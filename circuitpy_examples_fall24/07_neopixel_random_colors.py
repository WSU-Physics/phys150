# turn on random colors, one at a time
import time
import random
from adafruit_circuitplayground import cp

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.1

time_step = 1.0  # time between turning on pixels

for i in range(10):
    r = random.randint(0, 128)
    g = random.randint(0, 128)
    b = random.randint(0, 128)
    color = (r, g, b)
    cp.pixels[i] = color
    time.sleep(time_step)

# Now that we've turned on all the lights,
# keep the program running so it doesn't shut them off.
while True:
    time.sleep(1)
