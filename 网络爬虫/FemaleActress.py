import requests,re,time
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor

#pool = ProcessPoolExecutor(20)
def getActress(url):
    r=requests.get(url, timeout=30)
    #r.raise_for_status()
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,'html.parser')
    for j in soup.find_all('h3'):
        if re.search(name,j.string):
            print(i)
            print(j.string)
            
name=input('请输入关键词：')
for i in range(1,77):
    url='https://www.9956h.com/Html/100/index-{}.html'.format(i)
    #pool.submit(getActress, url)
    getActress(url)
time.sleep(1000)
