import json # import json module
import os
import shutil

# with statement
with open('metadata.json') as json_file:
    json_data = json.load(json_file)

    # 각 영상별 input ouput 위치
    # 4번 해야됨
    input_dir = "G:\\Facebook_main_image\\dfdc_train_part_04"
    input_list = os.listdir(input_dir)
    output_dir = "G:\\Facebook_main_image\\real_04\\"

    # output 폴더 없으면 생성
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for i in range(len(input_list)):
        #print(input_list[i][0:10])
        name = input_list[i][0:10]

        json_string = json_data[name+".mp4"]
        #print(json_string["label"])
        if "REAL" in json_string["label"] :
            print(json_string["label"])
            print(input_list[i])
            shutil.move(input_dir+"\\"+input_list[i],output_dir)