import numpy as np,pandas as pd
dates=pd.date_range('20180101',periods=3)
a=pd.DataFrame(np.arange(12).reshape((3,4)),index=dates,columns=['A','B','C','D'])
print(a)
print('-'*30)
#print(a[0:1])
#print(a['B'])
#by label
# print(a.loc['20180101'])
# print(a.loc[:,['A','B']])
# #by position
x = a.iloc[:,1]
for i in x:
	print(i)
#print(a.iloc[:,1])
# #mix label and position
# print(a.ix[:2,['A','C']])
# #Boolean
# print(a[a.A>4])
