import requests,bs4
from lxml import etree
url='http://www.gaokao.com/sichuan/fsx/'
r=requests.get(url)
r.raise_for_status()
r.encoding=r.apparent_encoding
soup=bs4.BeautifulSoup(r.text,'html.parser')
wen=soup.select('h3[class="blue ft14 txtC"]')[0].string
li=soup.select('h3[class="blue ft14 txtC lkTit"]')[0].string
yiben=etree.HTML(r.text).xpath('/html/body/div[3]/div[3]/div[2]\
                               /table[1]/tbody/tr[2]/td[1]')[0].string
print(yiben)
