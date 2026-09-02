# from adafruit
# these "import" commands should always be in your program.  they are libraries of commands that can be used in the program

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
