import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play
sound = AS.from_mp3('编程猫的梦想.mp3')
channels = sound.split_to_mono()
left = channels[0]
right = channels[1]
l_channel = AS.empty()
r_channel = AS.empty()
for i in range(0, len(sound), 5000):
    if i%10000 == 0:
        l_channel += left[i:i+5000].fade_in(1000).fade_out(1000)
        r_channel += right[i:i+5000].apply_gain(-120)
    else:
        l_channel += left[i:i+5000].apply_gain(-120)
        r_channel += right[i:i+5000].fade_in(1000).fade_out(1000)
dual = AS.from_mono_audiosegments(l_channel, r_channel)
print(dual.channels)
play(dual)
