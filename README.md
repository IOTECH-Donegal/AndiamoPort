# Andiamo-Port
This is a configuration for a complex boat with multiple instruments and RTK precision navigation.
As a RPi does not have a built-in RTC, it needs time synch at startup.
This configuration has always-on Internet via a Mi-Fi, it does not use SetUTC for time synch.

### Boats Brains

    Marinized RPi 3B+ identified by 

    - Ethernet: b8:27:eb:35:87:55
    - WiFi: b8:27:eb:60:d2:00

    All external interfacing is via a Zihatec RS422 hat.
    The boat has a Shipmodul NMEA0183/2000 multiplexor.

### Build

    Build from generic Raspbian Buster image
    Plug in Ethernet
    Go through startup Wizard
    Updates
    Change Hostname to AndiamoPort
    Enable VNC and SSH
    Change screen resolution to largest for remote login via VNC, 
    Reboot
    You may install OpenCPN and CM93 charts for test and verification.

### Configure Zihatec hat
    
    Check to make sure you DO NOT have /dev/ttyS0
    sudo raspi config
    3 - Interfacing
    6 - Serial
    Login shell available = no
    Serial port hardware = yes
    Exit and reboot
    After reboot, confirm you have /dev/ttyS0

### Network 

    This configuration assumes the boat has its own Mi-Fi
    Join Andiamo Mi-Fi radio network

### Devices
    The Zihatec hat is on /dev/ttyS0
    U-Blox will normally be /dev/ttyACM0 @ 38,400 
    NMEA via USB will probably be /dev/ttyUSB0 @ 4,800

### Autostart

    Copy across the most recent version of autoexec.py
    edit /etc/rc.local and add;
    
    sudo python3 /home/pi/autoexec.py & 
    exit 0
    
### Test

    Make sure system logs to the correct directory
    Make sure a fresh logfile is created after each reboot
    Insert a 32GB USB key and use SD Card Copier to create a backup. This should be done at the end of every day's survey.
