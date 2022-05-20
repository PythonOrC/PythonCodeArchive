import media_tool 
from pydub import AudioSegment as AS
from pydub.playback import play
import os

file='.'
files = os.listdir(file)
sound_ext = ['mp3','wav','ape','flac']
sounds = []
for file in files:
    ext = file.split('.')[-1]
    if ext in sound_ext:
        sound = AS.from_file(file, format=ext)
        sounds.append(sound)

songs = sounds[0]
for s in sounds[1:]:
    songs = songs.append(s, crossfade=300)
songs = songs.fade_in(1000).fade_out(1000)
play(songs)
