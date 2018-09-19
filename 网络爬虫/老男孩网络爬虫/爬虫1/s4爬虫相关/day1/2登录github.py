import requests
from bs4 import BeautifulSoup

# 获取token
r1 = requests.get('https://github.com/login')
s1 = BeautifulSoup(r1.text,'html.parser')
token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')
r1_cookie_dict = r1.cookies.get_dict()
# 讲用户名密码token发送到服务端，post
"""
utf8:✓
authenticity_token:ollV+avLm6Fh3ZevegPO7gOH7xUzEBL0NWdA1aOQ1IO3YQspjOHbfnaXJOtVLQ95BtW9GZlaCIYd5M6v7FGUKg==
login:asdf
password:asdf
commit:Sign in
"""
r2 = requests.post(
    'https://github.com/session',
    data={
        "utf8": '✓',
        "authenticity_token": token,
        'login': '317828332@qq.com',
        'password': 'alex3714',
        'commit': 'Sign in'
    },
    cookies=r1_cookie_dict
)
# print(r2.text)
# #
r2_cookie_dict = r2.cookies.get_dict()
cookie_dict = {}
cookie_dict.update(r1_cookie_dict)
cookie_dict.update(r2_cookie_dict)
#
r3 = requests.get(
    url='https://github.com/settings/emails',
    cookies=cookie_dict
)
print(r3.text)

