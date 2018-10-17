import pandas as pd, numpy as np
from lxml import etree

def list_to_str(list):
	return ''.join(list)

with open('1.html', encoding='utf-8') as f:
	html = f.read()

dom = etree.HTML(html)
row_list = []
i = 1
while 1:
	try:
		content = dom.xpath(f'//*[@id="nav01"]/tr[{i}]')[0]
	except:
		break
	user = list_to_str(content.xpath('./td[2]/text()'))
	name = list_to_str(content.xpath('./td[3]/input/@value'))
	qq = list_to_str(content.xpath('./td[4]/input/@value'))
	phone = list_to_str(content.xpath('./td[5]/input/@value'))
	mail = list_to_str(content.xpath('./td[6]/input/@value'))
	wechat = list_to_str(content.xpath('./td[7]/input/@value'))
	available = list_to_str(content.xpath('./td[9]/text()[1]'))
	date = list_to_str(content.xpath('./td[13]/text()'))
	recently_active = list_to_str(content.xpath('./td[14]/text()'))
	money = list_to_str(content.xpath('./td[15]/text()'))
	row_list.append([user,name,qq,phone,mail,wechat,available,date,recently_active,money])
	i += 1

row_array = np.array(row_list)
df = pd.DataFrame(row_array, columns=['用户名','姓名','QQ','手机','邮箱','微信','可用','注册时间','最近活跃','存款'])
df.to_excel('2.xls')