from moviepy.editor import *
import os

# file = open(fr"filenames_BIWI.txt", "r", encoding='utf-8') 
# file_list_biwi = file.readlines()
# file.close()

# file = open(fr"filenames_VOCASET.txt", "r", encoding='utf-8') 
# file_list_vocaset = file.readlines()
# file.close()

file = open(fr"filenames_multiface.txt", "r", encoding='utf-8') 
file_list_multiface = file.readlines()
file.close()

type = {
    'CodeTalker',
    'FaceFormer',
    'GT',
    'MeshTalk',
    'SelfTalk',
    'voca',
    'DiffSpeaker',
    'TalkingStyle',
    'FaceDiffuser'
}


# # BIWI
# for t in type:
#     for file in file_list_biwi:
#         pro = 'BIWI'
#         # 去掉每行末尾的换行符
#         file = file.strip()
#         video_path1 = f'render_video/{pro}/Ours/test_B/{file}'
#         video_path2 = f'render_video/{pro}/{t}/test_B/{file}'

#         # 加载两个视频文件

#         video1 = VideoFileClip(video_path1)
#         if os.path.exists(video_path2):
#             video2 = VideoFileClip(video_path2)
#         elif t=='SelfTalk' or t=='GT':
#             parts = video_path2.split('_')
#             video_path2 = parts[0] + '_' + parts[1] + '_' + parts[2] + '_' + parts[3] + '.mp4'
#             video2 = VideoFileClip(video_path2)
#         else:
#             path = video_path2.split("_condition")[0]
#             pre = f'render_video/{pro}/{t}/test_B/'
#             files = os.listdir(pre)
#             for f in files:
#                 f = pre + f
#                 if f.startswith(path):
#                     video2 = VideoFileClip(f)
#         # 确保视频时长相同
#         min_duration = min(video1.duration, video2.duration)
#         video1 = video1.set_duration(min_duration)
#         video2 = video2.set_duration(min_duration)

#         # 合并两个视频
#         final_clip = clips_array([[video1, video2]])

#         file_path = f"user_study/{pro}/{t}/{file}"
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)

#         # 保存最终合并后的视频
#         final_clip.write_videofile(file_path, codec='libx264')

# # VOCASET
# for t in type:
#     for file in file_list_vocaset:
#         pro = 'vocaset'
#         # 去掉每行末尾的换行符
#         file = file.strip()
#         video_path1 = f'render_video/{pro}/Ours/test/{file}'
#         video_path2 = f'render_video/{pro}/{t}/test/{file}'

#         # 加载两个视频文件
#         video1 = VideoFileClip(video_path1)
#         if os.path.exists(video_path2):
#             video2 = VideoFileClip(video_path2)
#         else:
#             path = video_path2.split("_condition")[0]
#             pre = f'render_video/{pro}/{t}/test/'
#             files = os.listdir(pre)
#             for f in files:
#                 f = pre + f
#                 if f.startswith(path):
#                     video2 = VideoFileClip(f)

#         # 确保视频时长相同
#         min_duration = min(video1.duration, video2.duration)
#         video1 = video1.set_duration(min_duration)
#         video2 = video2.set_duration(min_duration)

#         # 合并两个视频
#         final_clip = clips_array([[video1, video2]])

#         file_path = f"user_study/{pro}/{t}/{file}"
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         # 保存最终合并后的视频
#         final_clip.write_videofile(file_path, codec='libx264')

# multiface
for t in type:
    for file in file_list_multiface:
        pro = 'multiface'
        # 去掉每行末尾的换行符
        file = file.strip()
        video_path1 = f'render_video/{pro}/Ours/test_B/{file}'
        video_path2 = f'render_video/{pro}/{t}/test_B/{file}'

        # 加载两个视频文件

        video1 = VideoFileClip(video_path1)
        if os.path.exists(video_path2):
            video2 = VideoFileClip(video_path2)
        elif t=='SelfTalk' or t=='GT':
            parts = video_path2.split('_')
            video_path2 = parts[0] + '_' + parts[1] + '_' + parts[2] + '_' + parts[3] + '.mp4'
            video2 = VideoFileClip(video_path2)
        else:
            path = video_path2.split("_condition")[0]
            pre = f'render_video/{pro}/{t}/test_B/'
            files = os.listdir(pre)
            for f in files:
                f = pre + f
                if f.startswith(path):
                    video2 = VideoFileClip(f)
        # 确保视频时长相同
        min_duration = min(video1.duration, video2.duration)
        video1 = video1.set_duration(min_duration)
        video2 = video2.set_duration(min_duration)

        # 合并两个视频
        final_clip = clips_array([[video1, video2]])

        file_path = f"user_study/{pro}/{t}/{file}"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 保存最终合并后的视频
        final_clip.write_videofile(file_path, codec='libx264')