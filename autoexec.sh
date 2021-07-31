#!/bin/bash
# by: JOR
# Date: 30JUL21
# Function: autoexec for Linux
# Copy this script to /home/pi/
# To automate running this script, add the following to /etc/rc.local BEFORE the line exit 0
# sudo /home/pi/autoexec.sh
# Script: autoexec.sh


HOMEPATH="/home/pi"

#echo "Setting time from GPS"
#sleep 20
#sudo python3 $HOMEPATH/SetUTC/SetUTC.py 2>$HOMEPATH/SetUTC/SetUTC.err

python3 $HOMEPATH/SerialMux/SerialMux.py
