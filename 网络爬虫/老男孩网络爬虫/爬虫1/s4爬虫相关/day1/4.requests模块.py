import requests
# 1. 调用关系
# requests.get()
# requests.post()
# requests.put()
# requests.request('post')

# 2.常用参数

# url = 'xxx',
# params = {'k1': 'v1', 'nid': 888}, GET
# cookies = {},
# headers = {},
# data = {},
# json = {}

# requests.get(
#     url='xxx',
#     params={'k1':'v1','nid':888},
#     cookies={},
#     headers={}
# )
# http://www.baidu.com?k1=v2&nid=888
# requests.post(
#     url='xxx',
#     params={'k1':'v1','nid':888},
#     cookies={},
#     headers={},
#     data={},
#     json={}
# )
# 注意： 请求头
# application/x-www-form-urlencoded, request.POST
# requests.post(url='',data={},headers={'content-type': 'application/json'})
# requests.post(url='',data={},headers={'content-type': 'application/json'})
# requests.post(url='',json={})  # {'content-type': 'application/json'}


# def param_auth():
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

# ret = requests.get("http://192.168.1.1", auth=HTTPBasicAuth('wupeiqi', 'sdfasdfasdf'))
# ret = requests.get("http://192.168.1.1", auth=HTTPDigestAuth('wupeiqi', 'sdfasdfasdf'))
# ret = requests.get("http://192.168.1.1", headers={'Authorization': "asdfasdfasdfasf"})
# print(ret.text)

# ret = requests.get('http://192.168.1.1',
# auth=HTTPBasicAuth('admin', 'admin'))
# ret.encoding = 'gbk'
# print(ret.text)

# ret = requests.get('http://httpbin.org/digest-auth/auth/user/pass', auth=HTTPDigestAuth('user', 'pass'))
# print(ret)
#


# response = requests.get('http://www.adc.com',allow_redirects=True)
# print(response.text) # http://www.adc.com
# print(response.text) # http://www.baidu.com
#
# response = requests.get('url',stream=True)
# with open('') as f:
#     f.write('xxx')
# for line in response.iter_content():
#     pass
#
# response.close()
#
# from contextlib import closing
# with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
#     # 在此处理响应。
#     for i in r.iter_content():
#         print(i)


# 知乎，可带可不带，【知乎，xxxx】
# True,带
# False,不太
# 老男孩，必须
# requests.get('http://httpbin.org/get', stream=True,cert="xxxx.pem")




from bs4.element import Tag
# session,容器




