import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play
import os
import random

file = '.'
files = os.listdir(file)
sound_ext = ['mp3', 'wav', 'flac','ape']
music = {}
for file in files:
    ext = file.split('.')[-1]
    name = '.'.join(file.split('.')[:-1])
    if ext in sound_ext:
        sound = AS.from_file(file, format = ext)[3000:8000]
        music[name] = sound

songs = list(music.keys())
random.shuffle(songs)

for s in songs:
    play(music[s].reverse())
    answer = input()
    if answer == s:
        print('correct')
    else:
        print('incorrect',s)
