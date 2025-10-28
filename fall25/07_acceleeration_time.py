from adafruit_circuitplayground import cp
import time

counter = 0
num_steps = 100
sleep_time = 0.1

while True:

    while counter < num_steps:
        x, y, z = cp.acceleration
        t0 = time.monotonic()
        dt = counter * sleep_time
        print(x, ",", y, ",", z, ",", t0, ",", dt)
        time.sleep(sleep_time)
        counter = counter + 1# Write your code here :-)
