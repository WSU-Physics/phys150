#Adapted from
#https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/python-circuitpython
#https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython


import time
import math
import board
import digitalio
import busio
import adafruit_lis3dh
import microcontroller
import neopixel

#the acceleratometer has different ranges of precision. The default when using "cp" it is 4G
#I want the full precision so I can't use the "cp" library. Below I
# setup the pixels and accelerometer with the general circuit python libraries

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19,int1=int1)
lis3dh.range = adafruit_lis3dh.RANGE_2_G

num_average = 20 #the number of measurements to average together

pixels_hor = [5,6,7,8,9] #this pixels I plan to light up for horizontal
pixels_hor_range = [-20,-10,0,10,20] #the angle range for the 5 pixels
pixels_hor_2 = [0,1,2,3,4] #the pixels I plan to light up for vertical
pixels_hor_range_2 = [-20,-10,0,10,20] #the angle range fro the pixels
half_lighting_arc_length = 12 #the number of degrees away from the angle range that 
                                #I should start turning on the pixel


while True:
    x,y,z=0,0,0
    for measurement in range(0,num_average,1):
        #will loop and make measurements from the accelerometer for the num_average
        # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y, z
        # Divide them by 9.806 to convert to Gs. and adds the new measurements to the previous ones

        x = x + lis3dh.acceleration[0]/ adafruit_lis3dh.STANDARD_GRAVITY
        y = y + lis3dh.acceleration[1]/ adafruit_lis3dh.STANDARD_GRAVITY
        z = z + lis3dh.acceleration[2]/ adafruit_lis3dh.STANDARD_GRAVITY
    # Then divides by the num_average to get the average measurements
    x,y,z = (x/num_average,y/num_average,z/num_average)
    #computers the angle for horizontal
    if abs(x) > 0: 
        angle = math.atan(y/x)*180./math.pi
    else:
        angle = 90.0
    #computes the angle for the virticle
    if abs(y) > 0:
        angle_2 = math.atan(x/y)*180./math.pi
    else:
        angle = 90.0
    #print((angle,))


    for pixel in pixels_hor:
        delta_angle=pixels_hor_range[pixel-5]-angle
        if abs(delta_angle) >= half_lighting_arc_length:
            level = 0
        else:
            normalized_nearness = (1 - abs(delta_angle) / half_lighting_arc_length)
            level = int(normalized_nearness*50)
        print(level,angle)
        pixels[pixel] = (0, level, level)
        if abs(angle)< .2 and pixel==7:
            pixels[7]=(level*3,0,level*3)
            
    for pixel in pixels_hor_2:
        delta_angle=pixels_hor_range_2[pixel]-angle_2
        if abs(delta_angle) >= half_lighting_arc_length:
            level = 0
        else:
            normalized_nearness = (1 - abs(delta_angle) / half_lighting_arc_length)
            level = int(normalized_nearness*50)
        print(level,angle_2)
        pixels[pixel] = (0, level, level)
        if abs(angle_2)< .2 and pixel==2:
            pixels[2]=(level*3,0,level*3)
    pixels.show()
