import matplotlib.pyplot as plt
fig=plt.figure()
x=[1,2];y=[1,4]

left,bottom,width,height=0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_xlabel('x')

left,bottom,width,height=0.2,0.6,0.2,0.2
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'b')

plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside ')

plt.show()

