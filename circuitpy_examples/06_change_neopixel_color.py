# Make the neopixels blue, one at a time
import time
import random
from adafruit_circuitplayground import cp

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.1

time_step = 1.0  # time between turning on pixels
# Red, Green, Blue. 128 = max color
color = (0, 0, 128)

for i in range(10):
    # Turn on pixel i
    cp.pixels[i] = color
    time.sleep(time_step)

# Now that we've turned on all the lights,
# keep the program running so it doesn't shut them off.
while True:
    time.sleep(1)
