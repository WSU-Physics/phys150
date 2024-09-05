# Nathan Moore
#
import time
from adafruit_circuitplayground import cp

# 100% brightness is too much for me to look at.  This is an over-all setting.
cp.pixels.brightness = 0.05  # 5%

# set each color to 50/128 intensity
cp.pixels.fill((50, 50, 50))

while (True):

    for c in [1, 2, 3]:
        if (c == 1):
            b_Red = 64
            b_Green = 0
            b_Blue = 0
        elif (c == 2):            
            (b_Red,b_Green,b_Blue) = (0, 64, 0)
        elif (c == 3):
            (b_Red,b_Green,b_Blue) = (0, 0, 64)
            
        print("c=",c,"color=",b_Red, b_Green, b_Blue)

        for pn in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            cp.pixels[pn] = (b_Red, b_Green, b_Blue)
            time.sleep(0.1)
    
    cp.pixels.fill((50, 50, 50))
    time.sleep(0.5)
