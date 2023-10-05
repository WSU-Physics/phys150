from adafruit_circuitplayground import cp
import time
import math

cp.pixels.brightness = .2
grav = 9.8

while True:
    
    # loop over 10 measurements and take average
    sum_x = 0
    sum_y = 0
    sum_z = 0
    for i in [1,2,3,4,5,6,7,8,9,10]:
        x, y, z = cp.acceleration
        sum_x = sum_x + x
        sum_y = sum_y + y
        sum_z = sum_z + z
        
        time.sleep(0.05)
    # compute average, note that x is now an average
    x = sum_x/10.0
    y = sum_y/10.0
    z = sum_z/10.0


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
