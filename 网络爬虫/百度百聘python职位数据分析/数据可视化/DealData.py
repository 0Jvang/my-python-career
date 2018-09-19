import pandas as pd, numpy as np, matplotlib.pyplot as plt
from collections import Counter

def dealSalary_string(salary_string):
	'''
	根据该职位工资范围计算平均值
	'''
	try:
		if '-' in salary_string:
			min, max = salary_string.split('-')
			aver_salary = (eval(min) + eval(max)) / 2
		else:
			aver_salary = eval(salary_string[:-2])
	except:
		return ''
	return int(aver_salary)

def get_salary_list():
	'''
	获取工资list
	'''
	global data, salary_list
	data = pd.read_csv('JobInfo_csv')
	salary_list = []
	for i in data.iloc[:,2]:
		s = dealSalary_string(str(i))
		if s == '':
			continue
		salary_list.append(s)
	salary_list.sort()
	return salary_list

def get_city_list():
	data = pd.read_csv('JobInfo_csv')
	city_list = []
	for i in data.iloc[:,3]:
		if '市' in i:
			city_list.append(i.replace('市', ''))
		elif '/' in i:
			i = i.split('/')
			city_list.append(i[0])
			city_list.append(i[1])
		elif i == '广东':
			city_list.append('广州')
		elif i == '四川':
			city_list.append('成都')
		elif i == '浙江':
			city_list.append('杭州')
		elif i == '湖北':
			city_list.append('武汉')
		else:
			city_list.append(i)
	return city_list

def get_education_dict():
	data = pd.read_csv('JobInfo_csv')
	e = dict(data['education'])
	count = len(e)
	for i in range(count):
		if e[i] in ('本科以上', '统招本科'):
			e[i] = '本科'
		elif e[i] == '大专以上':
			e[i] = '大专'
	e = Counter(e.values())
	return e

def getSalary_xy(salary_list):
	'''
	获取去重工资列表x, 工资频数列表y
	'''
	global x, y
	y = []
	x = list(set(salary_list))
	for i in x:
		y.append(salary_list.count(i))
	return np.array(x), np.array(y)


