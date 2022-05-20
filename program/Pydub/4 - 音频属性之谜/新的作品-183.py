import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play

sound = AS.from_file('四句儿歌.mp3',format='mp3')
time = round(sound.duration_seconds, 3)
minutes = int(time//60)
seconds = round(time % 60)
print(str(minutes)+"\'"+str(seconds) + "\"")
print(str(sound.frame_rate)+ 'hz')
print("Avg: "+str(round(sound.dBFS))+'dB')
print("Max: "+str(round(sound.max_dBFS))+'dB')
