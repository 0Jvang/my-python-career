import matplotlib.pyplot as plt,numpy as np
x=np.linspace(-5,5,10)
y=x**2
#散点图
plt.figure()
plt.scatter(x,y,s=75,c='r',alpha=0.5)

#柱状图
plt.figure()
plt.bar(x,y,facecolor='b',edgecolor='w')
for x,y in zip(x,y):
    plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')

plt.show()
