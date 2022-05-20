# 导入os库
import os
# 导入工具文件
import media_tool
# 导入AudioSegment类
from pydub import Audiosegment
# 导入播放模块
# from pydub.playback import play
# 读取音频文件
# sound = AudioSegment.from_file("四句儿歌.mp3", format="mp3")
# 打印音频时长，单位为毫秒
# print(len(sound))
# # 打印音频时长，单位为秒
# print(f"音频时长约为：{sound.duration_seconds//60:.0f}分钟{sound.duration_seconds%60:.0f}秒")
# 读取音频帧数
# print(sound.frame_count())
# 1毫秒内的帧数
# # print(sound.frame_count(ms=1))
# 1秒内的帧数
# print(sound.frame_count(ms=1000))
# 音频的采样率
# print(sound.frame_rate)
# 播放采样率修改前的音频
# play(sound)
# 修改采样率为8000
# sound1 = sound.set_frame_rate(8000)
# 修改后的音频采样率
# print(sound1.frame_rate)
# 播放采样率修改后的音频
# play(sound1)
# 查询当前音频的分贝值
# print(sound.dBFS)
# 查询当前音频的最大分贝值
# print(sound.max_dBFS)

# 记录文件路径
filepath = "."
# 存放当前文件夹中的文件名称
files = os.listdir(filepath)
# 记录常见的音频类型
sound_ext = [".mp3", ".wav", ".ape", ".flac"]
# 遍历文件夹中的音频文件名称
for file in files:
    # 存储文件扩展
    ext = os.path.splitext(file)[-1]
    # 判断当前文件扩展名是否与音频类型相匹配
    if ext in sound_ext:
       # 获取当前文件的音频格式
       new_ext = ext[1:]
       # 读取当前音频文件
       sound = AudioSegment.from_file(file, format=new_ext)
       # 设置判断条件
       if sound.duration_seconds > 60 and sound.dBFS > -20 and sound.max_dBFS < 0:
           # 打印音频名称
           print(f"音频名称为：{file}")
           # 打印音频时长
           print(f"---音频时长约为：{sound.duration_seconds//60:.0f}分钟{sound.duration_seconds%60:.0f}秒")
           # 打印音频音量
           print(f"---音频最小音量约为：{sound.dBFS:.3f}，音频最大音量为：{sound.max_dBFS:.3f}")
