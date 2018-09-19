import jieba
text=open('雪山飞狐.txt',encoding='utf-8').read()
word=jieba.lcut(text)
count={}
exclude=('一个','说道','众人','自己','两人','心中','爹爹','金面佛',\
         '一声','不知','孩子','只是','只见')
for i in word:
    if len(i)==1 or len(i) >3 or i in exclude:
        continue
    count[i]=count.get(i,0)+1
print(count)
lst=list(count.items())
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=lst[i]
    print('{0:{2}<5}{1:}'.format(word,count,chr(12288)))
