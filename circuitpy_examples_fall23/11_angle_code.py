# this is the code we hacked out in class on 09-26  Doesn't quite work yet:
# divide by zero error needs to be fixed
# report degrees, not radians (as currently written)
# finally, need to figure out how to report this to users

# first two isssues resolved

from adafruit_circuitplayground import cp
import time
import math

cp.pixels.brightness = .2
grav = 9.8

while True:
    x, y, z = cp.acceleration
    r = int(abs(x / grav * 127))
    g = int(abs(y / grav * 127))
    b = int(abs(z / grav * 127))
    cp.pixels.fill([r, g, b])
    time.sleep(0.5)

    if x == 0.0 :
        theta_xy = 90.0 # degrees
        theta_xz = 90.0
    else:
        #2 pi radians in 360 degrees
        theta_xy = (360.0/(2.0*math.pi))*math.atan(y/x) # converted into degrees
        theta_xz = (360.0/(2.0*math.pi))*math.atan(z/x)

    if y==0.0 :
        theta_yz = 90.0
    else :
        theta_yz = (360.0/(2.0*math.pi))*math.atan(z/y)

    print( x, y, z, theta_xy, theta_xz, theta_yz )
