from konlpy.tag import *
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path="./NanumGothic.ttf"
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font',family=font_name)
path = "./comments/"
number = input("input folder name ")
number = str(number)
sub_path = path+number+"/"
output_path = './comments_output/'
ofolder_name = str(number)
output_path += ofolder_name
file = input("input file name(1~30)")
file = str(file)
textfile=file
textfile += '.txt'
wc_path = './clouds/'
wc_name = str(number)
wc_path += wc_name
f = open(sub_path+textfile, 'r', encoding='utf8')
op = open(output_path + '/' + textfile, 'w')
tokens = []
kkma = Okt()
while True:
    line = f.readline()
    if not line:
        break
    words = kkma.nouns(line)
    print(line)
    for word in words:
        op.write(word+' ')
op.close()
del f
del op
op = open(output_path+'/'+textfile,'r')
texts=op
for context in op:
    tokens += kkma.nouns(context)
    print(tokens)
wc=WordCloud(font_path=font_path,background_color="white").generate(' '.join(tokens))
#wc=wc.generate_from_text(sentence)
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
wc.to_file(wc_path+'/'+file+'.png')
#fig.savefig(wc_path+'/'+file)
