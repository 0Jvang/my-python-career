from pyecharts import Bar
from DealData import get_salary_list
from collections import Counter

s = get_salary_list()
s = Counter(s)
attr = list(s.keys())
value = list(s.values())
bar = Bar('工资分布', width = 1200, height = 600)
bar.add('', attr, value, xaxis_name = '工资', yaxis_name = '频数', is_more_utils = True)
bar.render()
