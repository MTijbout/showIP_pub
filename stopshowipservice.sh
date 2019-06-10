#!/bin/bash
#############################################################################
# Filename: stopshowipservice.sh
# Date Created: 03/15/19
# Author: Marco Tijbout
#
# Version 1.0
#
# Description: Script to be executed at login of user pi. This script will
#              stop the service showip.service and clear the sensehat
#              display.
#
# Usage: To have this script executed at login add the following to
#        .bash_profiile in the homedir of pi:
# if [ -f /opt/scripts/stopshowipservice.sh ]; then
# /opt/scripts/stopshowipservice.sh
# fi
#
# Version history:
# 1.0 - Marco Tijbout: First version of the script.
#############################################################################

# Stop the showip.service
sudo systemctl stop showip.service

# Clear the SenseHat display
/usr/bin/python3 /opt/scripts/clear.py