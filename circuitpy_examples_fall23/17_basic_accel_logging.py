from adafruit_circuitplayground import cp
import time

while True:
    x, y, z = cp.acceleration
    print((x,y,z))    # this line for interactive plotting
    time.sleep(wait_time)
