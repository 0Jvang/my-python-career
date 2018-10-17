import pandas as pd

dct = {}
df = pd.read_excel('data.xls', index_col=0)
df = df.sort_values(by='总分', ascending = False)
for i, j, k in zip(df.index, df['用户名'], df['总分']):
	if j in dct.keys():
		df.drop(i, inplace=True)
	else:
		dct[j] = k
df.to_excel('data2.xls', encoding='utf-8')


