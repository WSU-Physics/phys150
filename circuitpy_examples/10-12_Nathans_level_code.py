from adafruit_circuitplayground import cp
import time
import math

cp.pixels.brightness = .2
grav = 9.8

while True:

    # loop over N measurements and take average
    sum_x = 0
    sum_y = 0
    sum_z = 0
    num_readings_to_average = 20
    for i in range(num_readings_to_average):
        x, y, z = cp.acceleration
        sum_x = sum_x + x
        sum_y = sum_y + y
        sum_z = sum_z + z

        time.sleep(0.05)
    # compute average, note that x is now an average
    x = sum_x/(1.0*num_readings_to_average)
    y = sum_y/(1.0*num_readings_to_average)
    z = sum_z/(1.0*num_readings_to_average)


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

    print( x, y, z, "\t", theta_xy, theta_xz, theta_yz )

    # how far away from 90deg is each angle?
    dth_xy = 90-abs(theta_xy)
    dth_yz = 90-abs(theta_yz)
    dth_xz = 90-abs(theta_xz)
    
    # detect flat table (Z is up/down)
    # are t_xz and t_yz really close to 90 ?
    if (dth_xz<5 and dth_yz<5) :
        print ("flat table (Z is up/down)")
    
    # detect level (X is up/down)
    # are t_xz and t_xy really close to 90?
    if (dth_xz<5 and dth_xy<5) :
        print ("Level (X is up/down)")
        
    # detect plumb (Y is up down)
    # are t_yz and t_xy close to 90?
    if (dth_yz<5 and dth_xy<5) :
        print ("plumb (Y is up/down)")
