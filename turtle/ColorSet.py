import requests,bs4,time,re,random
from bs4 import BeautifulSoup
lst=[]
url='https://xkcd.com/color/rgb/'
try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
except:
    print('error')
soup=BeautifulSoup(r.text,'html.parser')
for i in soup.find_all('td'):
    a=i.find_all('center')
    c=re.findall(r'</div>(.*?)<br/>',''.join(str(a)))
    lst.append(''.join(c))
def Color():
    return random.choice(lst)

    
    
    
    
