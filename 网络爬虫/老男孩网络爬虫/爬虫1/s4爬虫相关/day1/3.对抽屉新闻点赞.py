# 1. 登录，cookie
# 2. 标签url，xxxx
import requests
from bs4 import BeautifulSoup

# 1. 获取cookie
r0 = requests.get('http://dig.chouti.com/')
r0_cookie_dict = r0.cookies.get_dict()

# 2. 发送用户名密码cookie
r1 = requests.post(
    'http://dig.chouti.com/login',
    data={
        'phone': '8615131255089',
        'password': 'woshiniba',
        'oneMonth':1
    },
    cookies=r0_cookie_dict
)
r1_cookie_dict = r1.cookies.get_dict()


# cookie_dict = {}
# cookie_dict.update(r0_cookie_dict)
# cookie_dict.update(r1_cookie_dict)

cookie_dict = {
    'gpsd': r0_cookie_dict['gpsd']
}

r2 = requests.post('http://dig.chouti.com/link/vote?linksId=13915601',cookies=cookie_dict)
print(r2.text)