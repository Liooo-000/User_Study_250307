import os

# 设置文件夹路径
dataset = 'MEAD'
folder_path = fr'user_study\{dataset}\GT'

# 设置输出文本文件的路径
output_file_path = fr'filenames_{dataset}.txt'

# 获取文件夹中所有文件和文件夹的名称
entries = os.listdir(folder_path)

# 打开文件准备写入
with open(output_file_path, 'w') as output_file:
    # 遍历所有条目
    for entry in entries:
        # 构建完整的文件或文件夹路径
        full_entry_path = os.path.join(folder_path, entry)
        # 检查是否是文件
        if os.path.isfile(full_entry_path):
            # 写入文件名到文本文件，每个文件名后跟一个换行符
            output_file.write(entry + '\n')

print("文件名已写入到文本文件。")