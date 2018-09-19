import requests, re, string
from bs4 import BeautifulSoup
from PIL import Image

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
           }
r1 = session.get('http://jwxt.swpu.edu.cn/loginAction.do', headers = headers)
img = session.get('http://jwxt.swpu.edu.cn/validateCodeAction.do')
with open('验证码.jpg','wb') as f:
    f.write(img.content)
img = Image.open('验证码.jpg')
img.show()
vcode = input('请输入验证码：')

r2 = session.post(
    'http://jwxt.swpu.edu.cn/loginAction.do',
    data = {
        'zjh':'201531010311',
        'mm':'635423',
        'v_yzm':string},
    headers = headers
    )

print(r2.text)

#r3 = requests.get('http://jwxt.swpu.edu.cn/bxqcjcxAction.do')
r3 = requests.get('http://jwxt.swpu.edu.cn/bxqcjcxAction.do', headers = headers, cookies = cookies)

soup = BeautifulSoup(r3.text, 'lxml')
tds = soup.find_all('td');print(tds)
