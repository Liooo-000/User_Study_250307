import os
import ffmpeg

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
            
            # 构建输出路径，将输出文件保存在对应的子文件夹结构中
            relative_path = os.path.relpath(root, input_dir)  # 获取相对路径
            output_folder = os.path.join(output_dir, relative_path)
            
            # 如果输出子文件夹不存在，则创建它
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            output_path = os.path.join(output_folder, filename)
            
            # 使用 ffmpeg-python 进行转码
            try:
                print(f"正在转换视频: {input_path}")
                (
                    ffmpeg
                    .input(input_path)
                    .output(output_path, vcodec='libx264')
                    .run(overwrite_output=True)  # 覆盖已存在的输出文件
                )
                print(f"转换完成: {output_path}")
            except Exception as e:
                print(f"视频 {filename} 转换失败: {e}")
