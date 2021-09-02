# Carl Ferkinhoff
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
    num_repeats=3 #sets how long at each brightness
    length = 180 #sets the length of the snore
    j=0
    brightness = .0     # initial (minimum) brightness is measured out of a max of 1.0
    T_fast = 0.01 #sets the period of the PWM
    while (j<length):
        #brightness increases
        i=0
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1
        j = j+1
        brightness = brightness+T_fast*90/length

    while (j>0):
        #brightness decreases
        i=0
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1
        j = j-1
        brightness = brightness-T_fast*90/length
