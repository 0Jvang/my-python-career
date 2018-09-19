import matplotlib.pyplot as plt
import matplotlib,numpy as np
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
labels=np.array(['综合','KDA','发育','推进','生存','输出'])
nattr=6
data=np.array([7,5,6,9,8,7])
angle=np.linspace(0,2*np.pi,nattr,endpoint=False)
data=np.concatenate((data,[data[0]]))                       #数组首尾闭合
angle=np.concatenate((angle,[angle[0]]))
fig=plt.figure(facecolor='white')
plt.subplot(111,polar=True)
plt.plot(angle,data,'bo-',color='blue',linewidth=1.5)
plt.fill(angle,data,facecolor='blue',alpha=0.25)
plt.thetagrids(angle*180/np.pi,labels)                      #给极坐标设置标签
plt.figtext(0.52,0.95,'dota能力值雷达图',ha='center')
plt.grid(True)                                                              #打开坐标网格
plt.savefig('dota_radar.JPG')
plt.show()

