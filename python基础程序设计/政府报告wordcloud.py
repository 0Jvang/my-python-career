import wordcloud,jieba,matplotlib.pyplot as plt
from scipy.misc import imread
mask=imread('maskPicture.jpg')
f=open('决胜小康.txt',encoding='utf-8').read()
txt=' ' .join(jieba.lcut(f))
w=wordcloud.WordCloud(font_path='simhei.ttf',\
                      background_color='yellow',max_words=50,mask=mask)
w.generate(txt)
w.to_file('决胜小康.jpg')
plt.axis('off')
plt.imshow(w)
plt.show()
