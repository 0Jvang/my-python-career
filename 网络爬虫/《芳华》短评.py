import requests,pandas as pd,numpy as np
from lxml import etree
file=[]
for i in range(2):
    url='https://movie.douban.com/subject/26862829/com\
ments?start={}&limit=20&sort=new_score&status\=P'.format(20*i)
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
    except:
        print("error")
    s=etree.HTML(r.text)
    file+=s.xpath('//*[@id="comments"]/div/div[2]/p/text()')
df=pd.DataFrame(file,columns=['短评'])
df=df.drop(16)
df=df.drop(30)
df.index =(i for i in range(1,41))
df.to_excel('芳华.xlsx',sheet_name='sheet1',header=False)
