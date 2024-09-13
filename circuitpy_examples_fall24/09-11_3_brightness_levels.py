# Modified from 03_dim_LED.py
# displaying 3 brightness levels
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

brightness = 0.01  # Choose a brightness between 0 and 1
period = 0.01  # Time per cycle, in seconds
T_on = brightness * period
T_off = period - T_on
N = 100

while True:
    brightness = 0.01  # Choose a brightness between 0 and 1
    T_on = brightness * period
    T_off = period - T_on
    for i in range(N):
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
    
    brightness = 0.10  # Choose a brightness between 0 and 1
    T_on = brightness * period
    T_off = period - T_on
    for i in range(N):
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        
    brightness = 0.40  # Choose a brightness between 0 and 1
    T_on = brightness * period
    T_off = period - T_on
    for i in range(N):
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
