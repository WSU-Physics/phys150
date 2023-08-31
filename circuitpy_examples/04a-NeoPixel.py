# Nathan Moore
# make the neopixels on a circuit playground dance
#
import time
import random
from adafruit_circuitplayground import cp

# 100% brightness is too much for me to look at.  This is an over-all setting.
cp.pixels.brightness  = 0.05 # 5%

# set each color to 50/128 intensity
cp.pixels.fill((50,50,50))

while (True):
    for pixel_number in [0,1,2,3,4,5,6,7,8,9]:
        # pixel number runs from 0->9
        # pixel color is Red-Green-Blue (RGB) and runs from 0->128
        b_Red = 64
        b_Blue = 0
        b_Green = 0
        cp.pixels[pixel_number]=(b_Red,b_Green,b_Blue)
        time.sleep(0.1)
        
    for pixel_number in [0,1,2,3,4,5,6,7,8,9]:
        b_Red = 0
        b_Green = 64
        b_Blue = 0
        cp.pixels[pixel_number]=(b_Red,b_Green,b_Blue)
        time.sleep(0.1)
        
    for pixel_number in [0,1,2,3,4,5,6,7,8,9]:
        b_Red = 0
        b_Green = 0
        b_Blue = 64
        cp.pixels[pixel_number]=(b_Red,b_Green,b_Blue)
        time.sleep(0.1)
    
    cp.pixels.fill((50,50,50))
    time.sleep(0.5)
