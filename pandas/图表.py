import pandas as pd,numpy as np,matplotlib.pyplot as plt
data=pd.DataFrame(np.random.randn(50,3),columns=list('ABC'))
data=data.cumsum()
#plot methods:
#bar,hist,box,kde,area,scatter,hexbin,pie
a=data.plot.scatter(x='A',y='B',color='red',label='1')
data.plot.scatter(x='A',y='C',color='blue',label='2',ax=a)
plt.show()

