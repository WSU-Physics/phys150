# this is a basic exampe from adafruit that spits ax, ay, az to serial
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython

import time
import math
from adafruit_circuitplayground.express import cpx


while True:
    x, y, z = cpx.acceleration
    #print((x,y,z))
    time.sleep(0.1)
    #angle_from_vertical = math.asin(y/9.81)
    if x == 0.0:
        angle_from_vertical = 90
    else:
        # compute the x/y angle from vertical
        angle_from_vertical = math.atan(y/x)*180/math.pi
    print((angle_from_vertical,))

    cpx.pixels.brightness = (1-(.95*abs(angle_from_vertical)/90))**5
    if abs(angle_from_vertical)< 0.3:
        cpx.pixels.fill((150,0,0))
    else:
        cpx.pixels.fill((50,50,50))
