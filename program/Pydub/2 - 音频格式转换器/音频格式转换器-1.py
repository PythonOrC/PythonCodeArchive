from pydub import AudioSegment as AS
from pydub.playback import play
import media_tool

while True:
    cmd = int(input('指令：'))
    if cmd == 1:
        filename_in = input('导入：')
        filename_out = input('输出：')
        aud = AS.from_file(filename_in, format=filename_in.split('.')[-1])
        aud.export(filename_out, format=filename_out.split('.')[-1])
    else:
        break
print('再见')
