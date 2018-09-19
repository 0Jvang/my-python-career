import pandas as pd
from pyecharts import Bar

data = pd.read_csv('JobInfo_csv')
e = data['experience'].value_counts()
attr = list(e.index)
value = list(e.values)
bar = Bar('经验要求', width = 1000, height = 500)
bar.add('', attr, value, xaxis_name = '经验', yaxis_name = '频数', is_more_utils = True)
bar.render()