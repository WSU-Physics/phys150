# Nathan Moore
# make the neopixels on a circuit playground dance
#
import time
import random
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
cp.pixels.fill((50,50,50))

start_time = time.time()
reset_interval=2.0
print(start_time)

while (True):
    random_pixel = random.randint(0,9)
    random_brightness_r = random.randint(0,128)
    random_brightness_g = random.randint(0,128)
    random_brightness_b = random.randint(0,128)
    cp.pixels[random_pixel]=(random_brightness_r,random_brightness_b,random_brightness_g)
    time.sleep(0.01)

    if( (time.time()-start_time) > reset_interval):
        print("reset")
        cp.pixels.brightness = 0.05
        for i in [0,1,2,3,4,5,6,7,8,9]:
            cp.pixels[i]=(0,0,0) # clearing out the pixels
            cp.pixels[i]=(50,50,50)  # this is the line that doesn't seem to execute on the second cp board.
            time.sleep(0.50)
        start_time = time.time()
