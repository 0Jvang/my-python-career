import matplotlib.pyplot as plt,numpy as np,matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
l1,=plt.plot(x,y1,color='red',linewidth=2,linestyle='--',\
             label='y1')
l2,=plt.plot(x,y2,label='y2')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y')

new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks=([-1,3],
            ['really bad','好'])

#gca='get current axis'
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#图例
plt.legend(handles=[l1,l2,],labels=['a','b'],loc='best')

#标注
plt.text(-1,2,'标注',fontdict={'size':16,'color':'r'})

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='k',edgecolor='None',\
                        alpha=0.3))
plt.show()








