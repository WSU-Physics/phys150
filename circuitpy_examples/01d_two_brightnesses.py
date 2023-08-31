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
    for brightness in [0.2, 0.4, 0.6, 0.8, 1.0, 0.6, 0.4, 0.2, 0]:
        # brightness is measured out of a max of 1.0
        T_fast = 0.01
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        num_repeats=30 
        i=0
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1
