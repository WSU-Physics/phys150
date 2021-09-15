import numpy as np
from scipy.io.wavfile import write

# Create a wav file to play on the circuit playground
# This example creates a "siren" sound going up and down in pitch

sample_rate = 8000  # samples/s
total_time = 5  # s
length = int(sample_rate * total_time)
freq_i = 200  # Hz
freq_f = 1600  # Hz

times = np.arange(length) / sample_rate
freqs = (np.sin(2 * np.pi * times / total_time - np.pi / 2) + 1) / 2 * (freq_f - freq_i) + freq_i
waveform = np.sin(2 * np.pi * np.cumsum(freqs / sample_rate))
waveform = np.int16(waveform * 2**14 + 2**14)

write("siren.wav", sample_rate, waveform)
