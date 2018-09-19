import pandas as pd,numpy as np
b=np.arange(12).reshape((3,4))
dates=pd.date_range('20180101',periods=3)
a=pd.DataFrame(b,index=dates,columns=['A','B','C','D'])
a.iloc[2,2]=1111
a.loc['20180103','D']=2222
a.B[a.A>1]=0
a['E']=np.nan
a['F']=pd.Series([1,2,3],index=dates)
print(a)
