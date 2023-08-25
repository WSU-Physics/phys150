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
    # option 1
    for i in [1, 2, 3, 4, 5, 4, 3, 2, 1]:
        print("Hello, CircuitPython!",i)
        led.value = True
        time.sleep(i/10)
        led.value = False
        time.sleep(i/10)
    #or, option 2
    i=1
    up=1
    while(i>0) :
        print("Hello, CircuitPython!",i)
        led.value = True
        time.sleep(i/10)
        led.value = False
        time.sleep(i/10)
        if(i==5):
            up=0
        if(up==1):
            i = i+1
        elif(up==0):
            i = i-1
        else:
            print("unexpected up value, stop?")
# Q: How could we use while loops and if statements to "buzz" out two different smoothed brightness levels?
