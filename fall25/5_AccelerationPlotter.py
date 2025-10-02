from adafruit_circuitplayground import cp
import time


while True:
    x, y, z = cp.acceleration
    print("(", x, ",", y, ",", z, ")")
    time.sleep(1)
# What line of code reads the accelerometer?
# What are the units of acceleration?
# How can you make the acceleration into an integer?
# Here's the Adafruit documentation for the accelerometer
# https://learn.adafruit.com/circuit-playground-lesson-number-0/accelerometer

