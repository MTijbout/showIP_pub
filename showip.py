#############################################################################
# Filename: showip.py
#
# Version 1.1
#
# Description: Display IP address on SenseHat useful when demoing Pulse/RPi in headless mode.
#
# Usage: Store this script in /opt/scripts
#
# Version history:
# 1.1 - Marco Tijbout: modified file locations and some clean-up.
# 1.0 - Ken Osborn: Original script.
#############################################################################

import os
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

b = (0, 0, 0)
f = (0, 100, 0)

#Write IP address to file and set variable
os.system("echo $(hostname -I | awk '{print$1}') > /opt/scripts/ip.txt")
filename = '/opt/scripts/ip.txt'

#echo current IP address
count = 0
while (count<3):
        #Read IP Address from file and display to SenseHat
        with open(filename) as file_object:
                for ip_address in file_object:
                        sense.show_message(ip_address, text_colour=f, back_colour=b, scroll_speed=0.07)
                        count=count+1

sense.clear()
