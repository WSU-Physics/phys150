# Adam Beardsley
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

# Choose a brightness between 0 and 1
brightness = .01
# Time per cycle, in seconds
period = 0.01

T_on = brightness * period
T_off = period - T_on

while True:
    led.value = True
    time.sleep(T_on)
    led.value = False
    time.sleep(T_off)
    # How can we use the buttons on the CPX to change the brightness while the program is running?
    # looking at the documentation, https://learn.adafruit.com/circuit-playground-lesson-number-0/buttons-slide-switch
    if(button_a):
        period = period*0.9
    if(button_b):
        period = period*1.1
    print(period)
        
# Try changing brightness and period and see if they do what you expect.
# Why are some commands outside the while loop, and others inside?
