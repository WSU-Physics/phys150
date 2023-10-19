from adafruit_circuitplayground import cp
import time

# wait time in s
wait_time = 0.1

while True:
    x, y, z = cp.acceleration
    t = time.monotonic() #https://docs.circuitpython.org/en/latest/shared-bindings/time/
    print(t,",",x,",",y,",",z,",") # this line for csv plotting
    #     print((x,y,z))    # this line for interactive plotting
    time.sleep(wait_time)
