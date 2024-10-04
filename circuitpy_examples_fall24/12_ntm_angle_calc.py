from adafruit_circuitplayground import cp
import time
import math

while True:
    x, y, z = cp.acceleration
    # calculate angle in degrees
    if(z!=0) :
        angle = (180.0/math.pi)*math.atan(x/z)
    else :
        angle = 90.0
    print("g/accel =(%5.2f, %5.2f, %5.2f)\tx-z angle = %.2f degrees"%(x,y,z,angle))
#    print("(",angle,",)") # formatted for the Mu Plotter
    time.sleep(1)

# Here's the Adafruit documentation for the accelerometer
#     https://learn.adafruit.com/circuit-playground-lesson-number-0/accelerometer
