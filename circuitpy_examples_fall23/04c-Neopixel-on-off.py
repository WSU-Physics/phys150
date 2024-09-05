# Nathan Moore
#
import time
from adafruit_circuitplayground import cp

# 100% brightness is too much for me to look at.  This is an over-all setting.
cp.pixels.brightness = 0.05  # 5%

# set each color to 50/128 intensity
cp.pixels.fill((50, 50, 50))

while (True):

    for pn in range(0,10,1):
        cp.pixels[pn] = (64, 0, 64)
        time.sleep(0.4)
        cp.pixels[pn] = (0, 0, 0)
        
    cp.pixels.fill((50, 50, 50))
    time.sleep(0.5)
    cp.pixels.fill((0, 0, 0))
