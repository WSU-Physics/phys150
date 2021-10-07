#https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
#RENAME the file to "boot.py" and save it to your circuit playground and the reset it.
#Then if you slide switch the right you can log data to your playground but can't edit your code.py file.
#move the switch to the left, press reset, and you will be able edit your code.py file.

import board
import digitalio
import storage

# For Gemma M0, Trinket M0, Metro M0/M4 Express, ItsyBitsy M0/M4 Express
#switch = digitalio.DigitalInOut(board.D2)

# For Feather M0/M4 Express
# switch = digitalio.DigitalInOut(board.D5)

# For Circuit Playground Express, Circuit Playground Bluefruit
switch = digitalio.DigitalInOut(board.D7)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", switch.value)
