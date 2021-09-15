from adafruit_circuitplayground import cp
import time
import random
import board
import digitalio
from audiocore import WaveFile
from audioio import AudioOut


# Enable the speaker
spkrenable = cp._speaker_enable
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# Play the siren noise.
# Use gen_wav_file.py to create the wav file.
wave_file = open('siren.wav', "rb")
wave = WaveFile(wave_file)
audio = AudioOut(board.SPEAKER)
audio.play(wave, loop=True)

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.1
time_step = 0.03  # time between turning on pixels
while True:
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        r = 0
        g = 0
        b = 255
        color = (r, g, b)
        cp.pixels[i] = color
        time.sleep(time_step)
    for i in [0, 1, 2, 3,4, 5, 6, 7, 8, 9]:
        r = 255
        g = 0
        b = 0
        color = (r, g, b)
        cp.pixels[i] = color
        time.sleep(time_step)
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        r = 0
        g = 0
        b = 0
        color = (r, g, b)
        cp.pixels[i] = color
        time.sleep(time_step)
