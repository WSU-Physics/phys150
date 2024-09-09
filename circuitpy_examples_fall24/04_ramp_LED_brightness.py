# Adam Beardsley
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ramp_time = 3  # Time to ramp up, in seconds
period = 0.01  # Time per cycle, in seconds
step = period / ramp_time  # how much to increment the brightness each cycle

while True:
    brightness = 0  # Start off
    while brightness < 1:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness += step

# Convince yourself the expression for step (line 14) is correct
# How can you *test* that step is correct?
# Can you reverse the program (start bright, get dim)
