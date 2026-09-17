#averageing angles measured by a CPy board.
from adafruit_circuitplayground import cp
import time
import math

# how many am I going to save for an average?
N_avg = 10
# angles I'm going to average
angles=[]

print("Hello")
while True:
    
    angles=[]
    for i in range(N_avg) :
        x, y, z = cp.acceleration
        # calculate angle in degrees
        if(z!=0) :
            angle = (180.0/math.pi)*math.atan(x/z)
        else :
            angle = 90.0
        angles.append(angle)
        
        time.sleep(1)

    # find average
    sum=0
    for b in angles:
        sum = sum+b
    average_angle = sum/N_avg
    
    print("recorded angles: ",angles)
    print("average = ",average_angle)
    

# Here's the Adafruit documentation for the accelerometer
#     https://learn.adafruit.com/circuit-playground-lesson-number-0/accelerometer
