# from adafruit

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# it is sometimes convenient to define the time at one spot in the program
dt = 1

while True:
    for state in [True, False]:
        led.value = state
        time.sleep(dt)

# Walk through the loops like the computer does and predict what will happen
# Then try it out and see if you were right.
# Try different combinations in the iterative list, e.g. [True, False, True]
