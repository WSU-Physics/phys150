# in-class example, Oct 16
import time
import math
from adafruit_circuitplayground import cp

read_delay = 0.2 # (s) how often do we sample acceleration? 0.2 seems good.
g=9.8 # (m/s^2) standard g value for acceleration

num_prints=0
while ( num_prints<20 ) :
    x, y, z = cp.acceleration
    a = math.sqrt(x*x+y*y+z*z)/g
    t = time.monotonic()
    print(t,a,x,y,z)
    time.sleep(read_delay)
    num_prints += 1

#output looks like:
#92.046 0.985078 0.0766094 0.114914 9.65278
#92.251 1.017 0.229828 0.306437 9.95922
#92.456 0.981598 0.306437 0.0766094 9.61448
#92.661 1.00135 0.344742 0.153219 9.806
#92.866 1.0008 0.153219 0.114914 9.806
