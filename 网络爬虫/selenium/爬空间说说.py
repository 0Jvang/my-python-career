import lxml, time, os
import pandas as pd, numpy as np
from selenium import webdriver
from lxml import etree

friend = '565163451'
os.mkdir(f'G:/proc/网络爬虫/selenium/{friend}')
user = '913536012'
pw = 'luoluoYAsuolong0'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://qzone.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys(user)
driver.find_element_by_id('p').send_keys(pw)
driver.find_element_by_id('login_button').click()
driver.switch_to.default_content()
driver.get(f'http://user.qzone.qq.com/{friend}/311')

next_num = 0
ls = []
while 1:
	for i in range(1, 6):
		height = 20000 * i
		strWord = 'window.scrollBy(0, '+str(height)+')'
		driver.execute_script(strWord)
		time.sleep(2)

	try:
		driver.switch_to.frame('app_canvas_frame')
		selector = etree.HTML(driver.page_source)
		divs = selector.xpath("//*[@id='msgList']/li/div[3]")

		filename = friend +'.txt'
		with open(filename, 'a') as f:
			for div in divs:
				name = div.xpath('./div[2]/a/text()')
				content = div.xpath('./div[2]/pre/text()')
				date = div.xpath('./div[4]/div[1]/span/a/text()')
				name = name[0] if name else 'none'
				content = content[0] if content else 'none'
				date = date[0] if date else 'none'
				print(name, content, date)
				ls.append([name, content, date])
	except Exception as e:
		print(e)
		pass

	data = pd.DataFrame(np.array(ls), columns=['name', 'content', 'date'])
	data.to_excel(f'G:/proc/网络爬虫/selenium/{friend}/{friend}第{next_num+1}页.xls', encoding='utf-8')
	if driver.page_source.find('pager_next_'+str(next_num)) == -1:
		break
	driver.find_element_by_id('pager_next_'+str(next_num)).click()
	next_num += 1
	driver.switch_to.parent_frame()





