import os

biwi_face = {
    "biwi_voca_ours_face": 0,
    "biwi_voca_voca_face": 0,
    "biwi_meshtalk_ours_face": 0,
    "biwi_meshtalk_meshtalk_face": 0,
    "biwi_faceformer_ours_face": 0,
    "biwi_faceformer_faceformer_face": 0,
    "biwi_codetalker_ours_face": 0,
    "biwi_codetalker_codetalker_face": 0,
    "biwi_selftalk_ours_face": 0,
    "biwi_selftalk_gt_face": 0,
    "biwi_diffspeaker_ours_face": 0,
    "biwi_diffspeaker_gt_face": 0,
    "biwi_talkingstyle_ours_face": 0,
    "biwi_talkingstyle_gt_face": 0,
    "biwi_facediffuser_ours_face": 0,
    "biwi_facediffuser_gt_face": 0,
    "biwi_gt_ours_face": 0,
    "biwi_gt_gt_face": 0,
}

biwi_lip = {
    "biwi_voca_ours_lip": 0,
    "biwi_voca_voca_lip": 0,
    "biwi_meshtalk_ours_lip": 0,
    "biwi_meshtalk_meshtalk_lip": 0,
    "biwi_faceformer_ours_lip": 0,
    "biwi_faceformer_faceformer_lip": 0,
    "biwi_codetalker_ours_lip": 0,
    "biwi_codetalker_codetalker_lip": 0,
    "biwi_selftalk_ours_lip": 0,
    "biwi_selftalk_gt_lip": 0,
    "biwi_diffspeaker_ours_lip": 0,
    "biwi_diffspeaker_gt_lip": 0,
    "biwi_talkingstyle_ours_lip": 0,
    "biwi_talkingstyle_gt_lip": 0,
    "biwi_facediffuser_ours_lip": 0,
    "biwi_facediffuser_gt_lip": 0,
    "biwi_gt_ours_lip": 0,
    "biwi_gt_gt_lip": 0,
}

keyname = {
    "voca": 0,
    "meshtalk": 1,
    "faceformer": 2,
    "codetalker": 3,
    'selftalk': 4,
    'diffspeaker': 5,
    'talkingstyle': 6,
    'facediffuser': 7,
    'gt': 8,
}


biwi_realism = {
    "biwi_voca_realism": 0,
    "biwi_meshtalk_realism": 0,
    "biwi_faceformer_realism": 0,
    "biwi_codetalker_realism": 0,
    "biwi_selftalk_realism": 0,
    "biwi_diffspeaker_realism": 0,
    "biwi_talkingstyle_realism": 0,
    "biwi_facediffuser_realism": 0,
    "biwi_gt_realism": 0,
}

biwi_lip_sync = {
    "biwi_voca_lip_sync": 0,
    "biwi_meshtalk_lip_sync": 0,
    "biwi_faceformer_lip_sync": 0,
    "biwi_codetalker_lip_sync": 0,
    "biwi_selftalk_lip_sync": 0,
    "biwi_diffspeaker_lip_sync": 0,
    "biwi_talkingstyle_lip_sync": 0,
    "biwi_facediffuser_lip_sync": 0,
    "biwi_gt_lip_sync": 0,
}

def main():
    folder_path = r"result/BIWI"
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        if "BIWI" in file_name:
            file_path = os.path.join(folder_path, file_name)
            
            with open(file_path, "r") as file:
                file_content = file.read()
                digits = [char for char in file_content if char.isdigit()]
                array = [int(digit) for digit in digits]
                
                count(array)
    compution()

def count(array):
    global biwi_face, biwi_lip
    face_indices = [
        [0, 9],
        [1, 10],
        [2, 11],
        [3, 12],
        [4, 13],
        [5, 14],
        [6, 15],
        [7, 16],
        [8, 17],
    ]  
    lip_indices = [
        [18, 27],
        [19, 28],
        [20, 29],
        [21, 30],
        [22, 31],
        [23, 32],
        [24, 33],
        [25, 34],
        [26, 35],
    ]  

    for key, value in biwi_face.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index in face_indices[idx]:
                    if element == 1 and "ours" in key:
                        biwi_face[key]+=1
                    if element == 0 and "ours" not in key:
                        biwi_face[key]+=1  

    for key, value in biwi_lip.items(): 
        for index, element in enumerate(array):
            for idx, name in enumerate(keyname):
                if name in key and index in lip_indices[idx]:
                    if element == 1 and "ours" in key:
                        biwi_lip[key]+=1
                    if element == 0 and "ours" not in key:
                        biwi_lip[key]+=1     

def compution():
    global biwi_face, biwi_lip
    global biwi_realism, biwi_lip_sync

    # # 遍历字典的键和值
    # for key, value in biwi_face.items():
    #     print(key, value)

    # for key, value in biwi_lip.items():
    #     print(key, value)

    face_keys = list(biwi_realism.keys())  # 获取字典的所有键并转换为列表
    face_values = list(biwi_face.values())  # 获取字典的所有值并转换为列表
    for i in range(0, len(face_values), 2):
        if i + 1 < len(face_values):  # 检查下一个索引是否存在，确保索引不越界
            biwi_realism[face_keys[int(i/2)]] = round((face_values[i] /(face_values[i] + face_values[i+1]))*100, 2)

    for key, value in biwi_realism.items():
        print(key, value)    
    print('\n')
    lip_keys = list(biwi_lip_sync.keys())  
    lip_values = list(biwi_lip.values())  
    for i in range(0, len(lip_values), 2):
        if i + 1 < len(lip_values):  
            biwi_lip_sync[lip_keys[int(i/2)]] = round((lip_values[i] /(lip_values[i] + lip_values[i+1]))*100, 2)

    for key, value in biwi_lip_sync.items():
        print(key, value)    

    return biwi_realism, biwi_lip_sync

if __name__=='__main__':
    main()

