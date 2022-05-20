import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play

sounds={}
sounds['1'] = AS.from_wav('Do.wav')
sounds['2'] = AS.from_wav('Re.wav')
sounds['3'] = AS.from_wav('Mi.wav')
sounds['4'] = AS.from_wav('Fa.wav')
sounds['5'] = AS.from_wav('Sol.wav')
sounds['6'] = AS.from_wav('La.wav')
sounds['7'] = AS.from_wav('Si.wav')
sounds['8'] = AS.from_wav('Do2.wav')

song = '12345550668655504454334324321110'
music = AS.empty()
for s in song:
    if s == '0':
        music+=AS.silent(335)
    else:
        music += sounds[s][100:435]
vocal = AS.from_mp3('人声.mp3')
music=music.overlay(vocal, gain_during_overlay=-5)
music.export('demo.mp3', format='mp3')