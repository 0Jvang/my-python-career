import pandas as pd,numpy as np
a1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
a2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'])
a3=pd.DataFrame(np.ones((3,4))*2,columns=['c','d','e','f'],index=[1,2,3]
                )
res=pd.concat([a1,a2,a3],axis=0,ignore_index=True)
print(res)
res2=pd.concat([a1,a2,a3],axis=0,join='inner',ignore_index=True)
#join_axes=[a1.index]
print(res2)
