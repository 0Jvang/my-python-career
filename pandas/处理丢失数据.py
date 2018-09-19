import pandas as pd,numpy as np
b=np.arange(12).reshape((3,4))
dates=pd.date_range('20180101',periods=3)
a=pd.DataFrame(b,index=dates,columns=['A','B','C','D'])
a.iloc[0,0]=np.nan
a.iloc[2,2]=np.nan
a.dropna(axis=1,how='any')#how={'any','all'}
a.fillna(value='空白')
a.isnull()
print(a)
print(np.any(a.isnull())==True)
