#############################################################################
# Filename: clear.py
# Date Created: 03/15/19
# Author: Marco Tijbout
# Description: Clear the SenseHat display.
# Usage: Store this script in /opt/scripts
#############################################################################

import os
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
