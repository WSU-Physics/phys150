from adafruit_circuitplayground import cp
import time
import adafruit_lis3dh
import math

cp.pixels.brightness = .2
grav = 9.8

cp._lis3dh.range = adafruit_lis3dh.RANGE_2_G

npoints = 100

def sum(data, sq=False):
    out = 0
    for d in data:
        if sq:
            out += d**2
        else:
            out += d
    return out

def std(data):
    out = sum(data, sq=True) / len(data) - (sum(data) / len(data))**2
    out = math.sqrt(out)
    return out


while True:
    datax = []
    datay = []
    dataz = []
    for i in range(npoints):
        x, y, z = cp.acceleration
        datax.append(x)
        datay.append(y)
        dataz.append(z)
    print((std(datax), std(datay), std(dataz)))


############

from adafruit_circuitplayground import cp
import time
import adafruit_lis3dh
import math

cp._lis3dh.range = adafruit_lis3dh.RANGE_2_G

npoints = 1000

while True:
    if cp.button_a:
        time.sleep(0.5)
        datax = 0
        datax2 = 0
        datay = 0
        datay2 = 0
        dataz = 0
        dataz2 = 0
        for i in range(npoints):
            x, y, z = cp.acceleration
            datax += x
            datax2 += x**2
            datay += y
            datay2 += y**2
            dataz += z
            dataz2 += z**2
        print((datax / npoints, datay / npoints, dataz / npoints))
        stdx = math.sqrt(datax2 / npoints - (datax / npoints)**2)
        stdy = math.sqrt(datay2 / npoints - (datay / npoints)**2)
        stdz = math.sqrt(dataz2 / npoints - (dataz / npoints)**2)
        print((stdx, stdy, stdz))



###################
from adafruit_circuitplayground import cp
import time
import adafruit_lis3dh
import math

cp.pixels.brightness = .2
grav = 9.8

cp._lis3dh.range = adafruit_lis3dh.RANGE_2_G

npoints = 1000


while True:
    x, y, z = cp.acceleration
    angle = 180 * math.acos(z / math.sqrt(x**2 + y**2 + z**2)) / math.pi
    print((angle,))
