# Andy Ferstl
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Initialize Button A
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

# Initialize Button B
button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

# Choose a brightness between 0 and 1
brightness = .01
# Time per cycle, in seconds
period = 0.01

T_on = brightness * period
T_off = period - T_on

while (T_on < period):
    led.value = True
    time.sleep(T_on)
    led.value = False
    time.sleep(T_off)
#     if button a pressed, decrease time on
#      if button b pressed, increase time on
    if button_a.value:
        T_on = T_on*0.9
        print("T_on= ",T_on)
    if button_b.value:
        T_on = T_on*1.1
        print(T_on)
