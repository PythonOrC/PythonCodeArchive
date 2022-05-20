import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play

sound_bcm = AS.from_mp3('四句儿歌编程猫.mp3')
sound_xk = AS.from_mp3('四句儿歌小可.mp3')

length = len(sound_bcm)-len(sound_xk)

if length > 0:
	sound_xk = AS.silent(length) + sound_xk
else:
	sound_bcm = AS.silent(abs(length))+sound_bcm

s_bcm = list(sound_bcm[5500::3000])
s_xk = list(sound_xk[5500::3000])

sing = AS.empty()
for i in range(len(s_bcm)):
	if i % 2 == 0:
		sing += s_bcm[i].fade_out(300).fade_in(300)
	else:
		sing += s_xk[i].fade_out(300).fade_in(300)
last_bcm = sound_bcm[11000:]
last_xk = sound_xk[11500:]
last = last_bcm.overlay(last_xk, position = 300)
start = sound_bcm[0:5500]
complete = start+sing+last
play(complete)