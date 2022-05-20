import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play
from pydub.silence import split_on_silence
import random

words_aud = AS.from_mp3('听写单词.mp3')
words = ['grade', 'different', 'keep', 'coffee', 'program', 'important']
sound_list = split_on_silence(words_aud,silence_thresh=-60, min_silence_len=2000)
sound_dict = dict(zip(words,sound_list))

random.shuffle(words)
silence = AS.silent(800)

for s in words:
    play(silence)
    play(sound_dict[s])
    answer=input('')
    if answer == s:
        print("Correct")
    else:
        print('Incorrect', s)