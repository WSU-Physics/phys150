# read the 3d acceleration and write it to the serial window
from adafruit_circuitplayground import cp
import time

# wait time in s
read_wait_time = 0.1 # seconds
recording_time = 10 # seconds

# set each color to 50/128 intensity
cp.pixels.brightness  = 0.05 # 10% brightness
cp.pixels.fill((50,0,0)) # red - not recording yet
time.sleep(1.0)

# start recording
cp.pixels.fill((0,50,0)) # green, now recording
t1 = time.monotonic()
dt=0 # how long have we been recording

while (dt<recording_time):
    x, y, z = cp.acceleration
    t = time.monotonic() #https://docs.circuitpython.org/en/latest/shared-bindings/time/
    print(t,",",x,",",y,",",z,",")
    time.sleep(read_wait_time)
    dt = t-t1

cp.pixels.fill((50,0,0))
time.sleep(3)
