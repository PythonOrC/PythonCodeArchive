from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave


THRESHOLD = 5050
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=1, rate=RATE,
    input=True, output=True,
    frames_per_buffer=CHUNK_SIZE)

num_silent = 0
snd_started = False

r = array('h')
silent=True
while silent:
        # little endian, signed short
    snd_data = array('h', stream.read(CHUNK_SIZE))
    if byteorder == 'big':
        snd_data.byteswap()
    r.extend(snd_data)

    silent = max(snd_data) < THRESHOLD
print('sound',max(snd_data))

