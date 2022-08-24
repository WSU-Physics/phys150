# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("Hello, CircuitPython!")
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)

# What happens if you change the first/second sleep time?
# What happens if both values are True?
# How can you make it blink faster?
# How fast can you _see_ it blink?
#     Is it a limitation of the LED or your eye? Can we test it?
# How does the brightness change if you blink really fast?
# Can you control how bright it is?
