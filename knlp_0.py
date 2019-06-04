from konlpy.tag import *
import os
import platform
import gflags
import time

print(platform.architecture())

path = "E:/crawler/comments/"
number = input("폴더명 입력(숫자)")
number = str(number)
sub_path = path+number+"/"
output_path = 'E:/crawler/comments_output/'
ofolder_name = str(number)
output_path += ofolder_name
file = input("파일명(1~30)")
file = str(file)
file += '.txt'
f = open(sub_path+file, 'r', encoding='utf8')
op = open(output_path + '/' + file, 'w')
while True:
    line = f.readline()
    if not line:
        break
    sentence = line
    kkma = Okt()
    print(kkma.nouns(line))
    words = kkma.nouns(line)
    for word in words:
        op.write(word+' ')
op.close()
del f
del op
del kkma
