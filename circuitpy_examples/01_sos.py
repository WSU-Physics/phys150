# Nathan's SOS code, inspired by class discussion
#
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

# set up the (red) LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    # this loop follows the same repetition as in the previous foreach example
    # reminder:     for a in [1,2,3,4,5]:
    # the diffrerence is the while (instead of foreach) loop structure
    for a in [1,1,1,3,3,3,1,1,1,]:
        print("Hello, CircuitPython!",a)
        led.value = True
        time.sleep(a/10)
        led.value = False
        time.sleep(0.2)
    time.sleep(2.0)
