# Adam Beardsley
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Choose a brightness between 0 and 1
brightness = .01
# Time per cycle, in seconds
period = 0.01

T_on = brightness * period
T_off = period - T_on

while True:
    led.value = True
    time.sleep(T_on)
    led.value = False
    time.sleep(T_off)
    # idea from the class, what if the buttons on the cipy changed the speed, how would we do that?

# Try changing brightness and period and see if they do what you expect.
# Why are some commands outside the while loop, and others inside?
# How could you change the brightness while the program is running?
