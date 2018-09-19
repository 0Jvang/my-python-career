import requests
from bs4 import BeautifulSoup

# 获取cookies
r1_cookie_dict = requests.get('https://www.taobao.com/').cookies.get_dict()
# 讲用户名密码token发送到服务端，获取登录cookie
r2 = requests.post(
    'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632360_8858797_29866178%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3D6f9dee79078282bdf1a3a5e52ce159ce%26upsid%3D6f9dee79078282bdf1a3a5e52ce159ce',
    data={
        'TPL_username':'18244215832',        
        'TPL_password':'IAMBLEACH2'       
    },
    cookies=r1_cookie_dict
)
r2_cookie_dict = r2.cookies.get_dict()

cookie_dict = {}
cookie_dict.update(r1_cookie_dict)
cookie_dict.update(r2_cookie_dict)
#带着登录后的cookie就可以访问任何页面
r3 = requests.get(
    url='https://item.taobao.com/item.htm?id=567007591580&ali_trackid=2:mm_133365862_45958709_732510042:1529651435_318_616436059&clk1=a9a8239711394cc14a72d838bf47e0bd&upsid=a9a8239711394cc14a72d838bf47e0bd',
    cookies=cookie_dict
)
vI3GE3c1t+xx9Xc2jf8quIsA8j5PKhRA0V1L9qk1+7bJEAeZvRK0iesY5QfV4qB4BqR+gOOxPxOvmpB+FVAlvA==