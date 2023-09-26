# this is the code we hacked out in class on 09-26  Doesn't quite work yet:
# divide by zero error needs to be fixed
# report degrees, not radians (as currently written)
# finally, need to figure out how to report this to users

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

    theta_xy = math.atan(y/x)
    theta_xz = math.atan(z/x)
    theta_yz = math.atan(z/y)

    print( x, y, z, theta_xy, theta_xz, theta_yz )



