# Write your code here :-)
from adafruit_circuitplayground import cp
import time
import math

counter = 0
num_steps = 100
sleep_time = 0.05
accel_limit = 1.3

g = 9.8  # (m/s^2) standard g value for acceleration


# initial setup
x, y, z = cp.acceleration
a1 = math.sqrt(x*x+y*y+z*z)/g
time.sleep(sleep_time)

x, y, z = cp.acceleration
a2 = math.sqrt(x*x+y*y+z*z)/g
time.sleep(sleep_time)

x, y, z = cp.acceleration
a3 = math.sqrt(x*x+y*y+z*z)/g
# how would you compute slope from these a1, a2, a3 values?
slope1 = a2 - a1
slope2 = a3 - a2


if ((a2 > accel_limit) and (slope1 > 0) and (slope2 < 0)) :
    print("peak found")

while (counter < num_steps) :
    x, y, z = cp.acceleration

# do the shuffle
    a1 = a2
    a2 = a3
    a3 = math.sqrt(x*x+y*y+z*z)/g

    t0 = time.monotonic()
    time.sleep(sleep_time)
    counter = counter + 1

    slope1 = a2 - a1
    slope2 = a3 - a2
    if ((a2 > accel_limit) and (slope1 > 0) and (slope2 < 0)) :
        print("peak found")
