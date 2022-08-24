# Turn on in a star pattern
import time
import random
from adafruit_circuitplayground import cp

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.1

time_step = 0.3  # time between turning on pixels

while True:
    for i in [0, 6, 3, 9, 5, 2, 8, 4, 1, 7]:
        r = random.randint(0, 128)
        g = random.randint(0, 128)
        b = random.randint(0, 128)
        color = (r, g, b)
        cp.pixels[i] = color
        time.sleep(time_step)
