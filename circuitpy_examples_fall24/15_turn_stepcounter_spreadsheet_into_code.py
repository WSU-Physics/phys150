import time
import math
from adafruit_circuitplayground import cp

read_delay = 0.05  # (s) how often do we sample acceleration? 0.2 seems good.
g = 9.8  # (m/s^2) standard g value for acceleration
accel_limit = 1.3

# initial setup
x, y, z = cp.acceleration
a1 = math.sqrt(x*x+y*y+z*z)/g
time.sleep(read_delay)

x, y, z = cp.acceleration
a2 = math.sqrt(x*x+y*y+z*z)/g
time.sleep(read_delay)

x, y, z = cp.acceleration
a3 = math.sqrt(x*x+y*y+z*z)/g
# how would you compute slope from these a1, a2, a3 values?

slope1=a2-a1
slope2=a3-a2

# is this a peak?
if( (a2>accel_limit) and (slope1 > 0) and (slope2 < 0) ):
    print("peak found")
# or, if you want to be wrong like Nathan
#if( a2>accel_limit) :
#    if( slope1 > 0) :
#        if( slope2 < 0 ):
#            print("peak found")
    
num_prints=0
while ( num_prints<100 ) :
    x, y, z = cp.acceleration
    # new data means the new guy becomes the old guy
    a1 = a2
    a2 = a3
    a3 = math.sqrt(x*x+y*y+z*z)/g
    t = time.monotonic()
    time.sleep(read_delay)
    num_prints += 1

    # initial setup
    slope1=a2-a1
    slope2=a3-a2

    # is this a peak?
    if( (a2>accel_limit) and (slope1 > 0) and (slope2 < 0) ):
        print("peak found")
            
