import board
import digitalio
import time
import math

# I'm going to make the brightness follow a sine wave
# So I want brightness ~ sin(t)
# But brightness can't be negative, so I need to shift it up and divide by two.

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

period = 5  # full snore cycle time, in secondds
cycle_time = 0.01  # Time per on/off cycle, in seconds
t = 0.0  # time variable

while True:
    brightness = (math.sin(2. * math.pi * t / period) + 1.) / 2.
    T_on = brightness * cycle_time
    T_off = cycle_time - T_on
    led.value = True
    time.sleep(T_on)
    led.value = False
    time.sleep(T_off)
    t += cycle_time
