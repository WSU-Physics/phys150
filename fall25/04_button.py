from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.2
pixi = 0
color = (128, 128, 128)
cp.pixels[pixi] = color

state=0
while True:
    if cp.button_a:
        cp.pixels[pixi] = (0, 0, 0)
        pixi = (pixi + 1) % 10
        cp.pixels[pixi] = color
        while cp.button_a:
            time.sleep(0.05)

# What happens when you push a button?
# What is the purpose of line 12?
# What is the mathematical operation happening on line 13?
# What does the while loop on lines 15-16 do?
# Can you make button b do something?# Write your code here :-)
