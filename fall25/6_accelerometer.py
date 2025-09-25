from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = .2
grav = 9.8

while True:
    x, y, z = cp.acceleration
    r = int(abs(x / grav * 127))
    g = int(abs(y / grav * 127))
    b = int(abs(z / grav * 127))
    cp.pixels.fill([r, g, b])
    time.sleep(0.05)

# What line of code reads the accelerometer?
# What are the units of acceleration?
# How does this code relay the acceleration information to the user?
# Would this make a good level? Why or why not?
#
# Here's the Adafruit documentation for the accelerometer
#     https://learn.adafruit.com/circuit-playground-lesson-number-0/accelerometer# Write your code here :-)
