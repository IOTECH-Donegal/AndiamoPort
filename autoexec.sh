#!/bin/bash
# by: JOR
# Date: 30JUL21
# Function: autoexec.bat for Linux
# Leave this script in /home/pi
# Script: autoexec.sh

# To automate running this script, add the following to /etc/rc.local BEFORE the line exit 0
# sudo /home/pi/autoexec.sh

HOMEPATH="/home/pi"

echo "Setting time from GPS"
sleep 20
sudo python3 $HOMEPATH/SetUTC/SetUTC.py 2>$HOMEPATH/SetUTC/SetUTC.err

python3 $HOMEPATH/SerialMux/SerialMux.py
