import jieba,matplotlib.pyplot as plt
from wordcloud import WordCloud
wc=WordCloud(max_words=15,height=600,width=600,\
             font_path='simhei',background_color='black')
def getText(name):
    txt=open(name+".txt", "r",encoding='utf-8').read()
    word=jieba.lcut(txt)
    return word

def dealWords(lst):
    #射雕exclude={'比武招亲','华山论剑','欧阳克笑','亢龙有悔','成吉思汗','完颜洪烈','一灯大师','灵智上人','江南七怪','九阴真经','降龙十八掌','打狗棒法','完颜洪熙'}
    #神雕exclude=('金轮法王','武氏兄弟','公孙谷主','一灯大师','公孙绿萼','玉女心经','打狗棒法','九阴真经','史氏兄弟','......')
    exclude=('空闻大师','司徒千钟','空智大师','黄衫女子','灭绝师太','金花婆婆','武当七侠','掌棒龙头','执法长老','传功长老','掌钵龙头','铁冠道人')
    counts={}
    lst_wc=[]
    for i in lst:
        if len(i)<4:
            continue
        else:
            i=i
        lst_wc.append(i)
        counts[i]=counts.get(i,0)+1
    for i in exclude:
        del counts[i]
        while lst_wc.count(i):
            lst_wc.remove(i)
    lst_split=' '.join(lst_wc)
    wordcloud=wc.generate(lst_split)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    wc.to_file('倚天.jpg')
    words=list(counts.items())
    words.sort(key=lambda x:x[1],reverse=True)
    return words

def printFreq(dct):
    for i in range(15):
        word,count=dct[i]
        print("{:<10}{:>5}".format(word,count))

def main():
    name=input('请输入文档名：')
    lst=getText(name)  
    dct=dealWords(lst)
    printFreq(dct)

main()
