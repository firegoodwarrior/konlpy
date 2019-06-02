from konlpy.tag import *
import os
import platform

print(platform.architecture())

path = "E:/crawler/comments/"
folder_list = os.listdir(path)
number = 0
for folder in folder_list:
    sub_path = path+folder+"/"
    file_list = os.listdir(sub_path)
    output_path = 'E:/crawler/comments_output/'
    ofolder_name = str(number)
    output_path += ofolder_name
    file_name = '/result.txt'
    op = open(output_path+file_name, 'w')
    for file in file_list:
        f = open(sub_path+file, 'r', encoding='utf8')
        while True:
            line = f.readline()
            if not line:
                break
            sentence = line
            kkma = Okt()
            print(kkma.nouns(line))
            words = kkma.nouns(line)
            for word in words:
                op.write(word)

    op.close()