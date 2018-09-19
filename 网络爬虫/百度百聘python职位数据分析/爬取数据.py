import requests, json
import pandas as pd, numpy as np

def getJob(url): 
	'''
	获取职位信息
	'''
	r = requests.get(url)
	json_dict = json.loads(r.text)
	items = ['title', 'salary', 'ori_city', 'education', 'experience', 'description']
	for i in range(20):
		onejob_list = []
		for item in items:
			pattern = json_dict['data']['main']['data']['disp_data'][i][item].replace('\n', '').strip()
			onejob_list.append(pattern)
		lst.append(onejob_list)

lst = []
for i in range(0, 741, 20):
	url = f'http://zhaopin.baidu.com/api/quanzhiasync?query=python工作&sort_type=1&city_sug=泸州&detailmode=close&rn=20&pn={i}'
	getJob(url)

##data = pd.DataFrame(np.array(lst), columns=['name', 'salary', 'city', 'education', 'experience', 'description'])
##data.to_csv('JobInfo_csv', encoding='utf-8')
##data.to_excel('JobInfo_excel.xls', encoding='utf-8')
