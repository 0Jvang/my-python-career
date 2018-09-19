import matplotlib.pyplot as plt, numpy as np, pandas as pd, matplotlib
from DealData import getSalary_list, getSalary_xy

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False

def salary_hist(salary_list):
	'''
	画直方图
	'''
	plt.hist(salary_list, bins = 60, edgecolor = 'black')
	plt.xlabel('工资')
	plt.ylabel('频数')
	plt.title('工资分布直方图')
	plt.show()

def salary_scatter(x, y):
	'''
	画散点图
	'''
	plt.scatter(x, y, s = 40, c = np.array(y), alpha = 1)
	plt.xlabel('工资')
	plt.ylabel('频数')
	plt.title('工资分布散点图')
	plt.colorbar()
	plt.show()

def subplot():
	'''
	多图
	'''
	plt.figure()
	ax1 = plt.subplot2grid((1,2), (0,0), rowspan = 1, colspan = 1)
	ax1.hist(salary_list, bins = 60, edgecolor = 'black')
	
	ax2 = plt.subplot2grid((1,2), (0,1), rowspan = 1, colspan = 1)
	ax2.scatter(x, y, s = 40, c = np.array(y), alpha = 1)
	plt.show()
	
salary_list = getSalary_list()
x, y = getSalary_xy(salary_list)
salary_hist(salary_list)
salary_scatter(x, y)
subplot()
