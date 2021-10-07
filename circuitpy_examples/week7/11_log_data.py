# Adapted from AstroDocCarl:
# https://github.com/ntmoore/phys150_fall20/blob/master/10_1_log_acceleration_CDF.py

# Which is:
# Adapted from
# https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/python-circuitpython
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out

import time
from adafruit_circuitplayground.express import cpx
import os

g = 9.801
log_time = 0.02  # Time to wait between logging points
wait_time = 0.1  # Time to wait when listening for button


def get_fname():
    fname = "acceleration.csv"
    allfiles = os.listdir("/")

    if fname in allfiles:
        i = 1
        while fname in allfiles:
            print(i)
            fname = f"acceleration_{i}.csv"
            i += 1
    return "/" + fname

def log_accel(file=None):
    x, y, z = cpx.acceleration
    current_time = time.monotonic()
    outstr = f'{current_time},{x / g},{y / g},{z / g}\n'
    if file is not None:
        file.write(outstr)
        outstr = 'logging: ' + outstr
    print(outstr)
    return

def get_accel_on_button(file):
    cpx.red_led = False
    while not cpx.button_a:
        log_accel()
        time.sleep(wait_time)

    cpx.red_led = True
    while cpx.button_a:
        log_accel(file)
        time.sleep(log_time)
    file.flush()

    return

# See if a file is writeable, if it is it continues, if not it goes to the except statement
try:
    while True:
        # open a file to save the data to
        fname = get_fname()
        with open(fname, "a") as fp:
            get_accel_on_button(fp)

# will flash the D13 red LED to let us know we can edit the code.py file (i.e. the storage is writeable)
except OSError as e:
    delay = 1.0
    if e.args[0] == 28:
        # If file system is full, blink faster
        delay = 0.2
    while True:
        cpx.red_led = True
        time.sleep(delay)
        cpx.red_led = False
        time.sleep(delay)
