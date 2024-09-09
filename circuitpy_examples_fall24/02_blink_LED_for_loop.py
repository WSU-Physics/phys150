# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# ntm - I like specifying time in one place per class discussion
dt = 1

while True:
    for state in [True, False]:
        led.value = state
        time.sleep(dt)

# Walk through the loops like the computer does and predict what will happen
# Then try it out and see if you were right.
# Try different combinations in the iterative list, e.g. [True, False, True]
