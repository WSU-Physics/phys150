# Nathan Moore
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
    i=1
    # Note the while runs until the test, (i<6), fails
    while(i<6):     
        print("Hello, CircuitPython!",i)
        led.value = True
        time.sleep(i/10)
        led.value = False
        time.sleep(i/10)
        # "i"  is called a "counter" or "index" variable
        i = i+1
       
# Q: how could we get the program to count back down after counting up?
