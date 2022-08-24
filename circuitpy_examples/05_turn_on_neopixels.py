# Turn on the neopixels, one at a time
import time
import random
from adafruit_circuitplayground import cp

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.1

time_step = 1.0  # time between turning on pixels

for i in range(10):
    # Turn on pixel i
    cp.pixels[i] = (128, 128, 128)
    time.sleep(time_step)

# Now that we've turned on all the lights,
# keep the program running so it doesn't shut them off.
while True:
    time.sleep(1)
