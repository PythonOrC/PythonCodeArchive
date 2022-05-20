import media_tool
from pydub import AudioSegment as AS
from pydub.playback import play
import os


filename = '海棠不言 - 编程猫的梦想.mp3'
if os.path.exists(filename):
    filetype = filename.split('.')[-1]
    if filetype == 'mp3' or filetype == 'wav':
        aud = AS.from_file(filename, format= filetype)
        play(aud)
else:
    print('失败')


