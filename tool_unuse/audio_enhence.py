import os
import ffmpeg
from pydub import AudioSegment
import shutil

# 定义输入文件夹和输出文件夹路径
input_dir = r'user_study1'
output_dir = r'user_study'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        # 检查文件扩展名，确保处理的是视频文件（如 .mp4）
        if filename.endswith(".mp4"):
            input_path = os.path.join(root, filename)
            
            # 使用 pydub 检测音频音量
            audio = AudioSegment.from_file(input_path)
            loudness = audio.dBFS  # 获取音频的平均音量（分贝）

            # 设定阈值，如果音量低于该值，则增加音量
            threshold = -30.0  # 可以根据需要调整此值
            print(loudness)
            if loudness < threshold:
                print(f"正在转换视频: {input_path}")
                output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
                
                # 创建输出文件夹
                output_folder = os.path.dirname(output_path)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                
                # 增加音量并保存
                increased_audio = audio + threshold - loudness + 10  # 增加至threshold
                increased_audio.export("temp_audio.mp3", format="mp3")  # 导出临时音频文件

                # 将修改后的音频合并回视频
                video_input = ffmpeg.input(input_path)
                audio_input = ffmpeg.input("temp_audio.mp3")  # 先定义音频输入
                (
                    ffmpeg
                    .output(video_input, audio_input, output_path, 
                            vcodec='libx264', 
                            acodec='aac', 
                            audio_bitrate='192k', 
                            shortest=None)  # shortest用于处理音频长度不匹配的问题
                    .run(overwrite_output=True)  # 覆盖已存在的输出文件
                )
                
                print(f"音量已增加，转换完成: {output_path}")
            else:
                # 如果音量不低于阈值，则将原始视频复制到输出文件夹
                output_path = os.path.join(output_dir, os.path.relpath(input_path, input_dir))
                output_folder = os.path.dirname(output_path)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                
                shutil.copy(input_path, output_path)  # 复制原始视频
                print(f"音量正常，已复制视频: {output_path}")
                

# 删除临时文件
if os.path.exists("temp_audio.mp3"):
    os.remove("temp_audio.mp3")
