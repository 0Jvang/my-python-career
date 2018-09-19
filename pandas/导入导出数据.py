import pandas as pd
data=pd.read_csv('csv')
print(data)
data.to_pickle('excel_pickle')
data.to_csv('csv',index=False)
