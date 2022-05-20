from pydub import AudioSegment as AS
import media_tool
from pydub.utils import mediainfo
import os

aud = AS.from_mp3('四句儿歌.mp3')
filepath = '.'
files = os.listdir(filepath)
print(files)
sound_ext = ['mp3', 'flac', 'wav', 'ape']
folder = 'music'

for file in files:
    ext = file.split('.')[-1]
    if ext in sound_ext:
        song = AS.from_file(file, format=ext)
        aud.export(folder+'/'+file, format='mp3', tags={"album": "Best of 2020",
                                                        'comments': 'this album is awesome!'}, cover='专辑封面.jpg', id3v2_version='3')