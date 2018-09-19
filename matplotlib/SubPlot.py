import matplotlib.pyplot as plt
plt.figure()

ax1=plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3)
ax1.plot([1,2],[1,2])
ax1.set_title(ax1)

ax2=plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=2)
ax2.plot([1,2],[1,2])

ax3=plt.subplot2grid((3,3),(1,2),rowspan=2,colspan=1)
ax3.plot([1,2],[1,2])

ax4=plt.subplot2grid((3,3),(2,0),rowspan=1,colspan=1)
ax4.plot([1,2],[1,2])

ax5=plt.subplot2grid((3,3),(2,1),rowspan=1,colspan=1)
ax5.plot([1,2],[1,2])

plt.show()

    

