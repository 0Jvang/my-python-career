import requests,re
from lxml import etree
def getHTML(url):
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r
         
url='https://www.9969r.com/Html/63/index-{}.html'.format(2)
r=getHTML(url)
hrefs=re.findall(r'<a href="/Html/63/([0-9]{5})',r.text)
for href in hrefs:
    r2 = getHTML('https://www.9969r.com/Html/63/'+href+'.html')
    title=re.findall('<h1>(.*?)</h1>',r2.text)[0]
    for img in re.findall(r'<img src="(.*?)"/>',r2.text):    
        with open('picture/'+title+'.jpg','wb') as f:
            f.write(requests.get(img).content)



