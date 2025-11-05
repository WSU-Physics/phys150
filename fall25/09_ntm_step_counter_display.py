from adafruit_circuitplayground import cp
import time
import math

# set up neopixels
cp.pixels.brightness = 0.1

counter = 0
num_steps_to_find = 100
num_steps = 0
sleep_time = 0.1
accel_limit = 1.3
g = 9.8  # (m/s^2) standard g value for acceleration

# initial setup for slope measurement
x, y, z = cp.acceleration
a1 = math.sqrt(x*x+y*y+z*z)/g
time.sleep(sleep_time)

x, y, z = cp.acceleration
a2 = math.sqrt(x*x+y*y+z*z)/g
time.sleep(sleep_time)

x, y, z = cp.acceleration
a3 = math.sqrt(x*x+y*y+z*z)/g
# how would you compute slope from these a1, a2, a3 values?
#slope1 = a2 - a1
#slope2 = a3 - a2
# This is the typical peak-finding approach
#if ((a2 > accel_limit) and (slope1 > 0) and (slope2 < 0)) :
#    print("peak found")

while (num_steps < num_steps_to_find) :
    
    time.sleep(sleep_time)
    x, y, z = cp.acceleration

    # do the shuffle, move the stencil
    a1 = a2
    a2 = a3
    a3 = math.sqrt(x*x+y*y+z*z)/g

    slope1 = a2 - a1
    slope2 = a3 - a2
    if ((a2 > accel_limit) and (slope1 > 0) and (slope2 < 0)) :
        print("peak found")
        num_steps = num_steps + 1
        
        # display number of steps
        print("steps = ",num_steps," or (binary) ",bin(num_steps) )
        count = bin(num_steps)
        count = count[2:]
        print("pattern to write out is: ",count)
        
        # default to all written out as green
        lights=[2,2, 2,2,2,2, 2,2,2,2]
        
        # write out the pattern to the lights list
        for i in range(len(count)):
            lights[i] = int(count[i])
        print(lights)
        
        # write out the pattern to the Neopixels
        # green = nothing
        # blue = 1 (binary)
        # red = 0 (binary)
        for i in range(len(lights)):
            if(lights[i]==0) :
                cp.pixels[i] = (128,0,0)
            if(lights[i]==1) :
                cp.pixels[i] = (0,0,128)
            if(lights[i]==2) :
                cp.pixels[i] = (0,16,0)
            
