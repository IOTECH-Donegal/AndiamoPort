""""
Main routine to time sync a Linux server which is not network connected.
Assume Serial1 is a GPS
Tested with Python >=3.6 on RPi running Buster
By: JOR
    v0.1    06JUN20     First go using ZDA
    v0.2    20FEB21     Modified for RMC
    v0.3    30JUL21     Modified for AndiamoPort
"""

import os
import serial
import logging

print('This utility run at startup to set time and date on RPi')
print('Accuracy no better than 1 second')
logging.basicConfig(filename='/home/pi/SetUTC/SetUTC.log', level=logging.INFO)
logging.info('Started SetUTC.py')

try:

    # Configure the first serial port, this should be the master GPS
    # UBlox USB defaults to ttyACM0
    # Hardware serial defaults to ttyS0

    Serial_Port1 = serial.Serial(
        port='/dev/ttyS0',
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        rtscts=True,
        dsrdtr=True,
        timeout=1
    )
    Serial_Port1.flushInput()

 while True:
        read_buffer1 = Serial_Port1.readline().decode('ascii', errors='replace')
        nmea_full_sentence = str(read_buffer1)

        if nmea_full_sentence[0] == '$':

            # Break it up into fields
            list_of_values = nmea_full_sentence.split(',')
            # Process the talker ID and assign it to a property
            if list_of_values[0] == '$GNRMC':
                # Get time in the form 114645.00
                utctime = list_of_values[1]
                utchour = utctime[0:2]
                utcmin = utctime[2:4]
                utcsec = utctime[4:6]
                # Get dat in form DDMMYY
                utcdate = list_of_values[9]
                day = utcdate[0:2]
                month = utcdate[2:4]
                year = utcdate[4:6]      
                system_date = year + '-' + month + '-' + day
                system_time = utchour + ':' + utcmin + ':' + utcsec
                time_string = system_date + " " + system_time
                message = 'Used RMC to set the time to {} '.format(time_string)
                logging.info(message)
                os.system('sudo date -u --set "%s" ' % time_string)
                break

            if list_of_values[0] == '$GNZDA':
                # Get time in the form 114645.00
                utctime = list_of_values[1]
                utchour = utctime[0:2]
                utcmin = utctime[2:4]
                utcsec = utctime[4:6]
                day = list_of_values[2]
                month = list_of_values[3]
                year = list_of_values[4]
                system_date = year + '-' + month + '-' + day
                system_time = utchour + ':' + utcmin + ':' + utcsec
                time_string = system_date + " " + system_time
                message = 'Used ZDA to set the time to {} '.format(time_string)
                logging.info(message)
                os.system('sudo date -u --set "%s" ' % time_string)
                break

except serial.SerialException:
    logging.info('SetUTC failed to open the GPS')
    print('Error opening serial port...is the GPS connected?')
    exit(0)


    
    
    
