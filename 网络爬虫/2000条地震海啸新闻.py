import requests
from lxml import etree
def getHTML(url):
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text

url ='http://news.sina.com.cn/z/sumatraearthquake/3.shtml'
count = 1978
t = getHTML(url)  
hrefs = etree.HTML(t).xpath('/html/body/center/table[3]/tbody/tr/td[3]/span/li/a/@href')

for href in hrefs[:30]:
    t2 = getHTML(href)
    s=''
    for i in etree.HTML(t2).xpath('//*[@id="zoom"]/p/text()'):
        s = s+i
    with open('海啸/'+str(count)+'.txt','w',encoding='utf-8') as f:
        f.write(s)
    count+=1
##except:
##    print(count)
##    pass

