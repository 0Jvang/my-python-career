import numpy as np,matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)
x=np.arange(-4,4,0.25)
y=np.arange(-4,4,0.25)
x,y=np.meshgrid(x,y)
r=np.sqrt(x**2+y**2)
z=np.sin(r)

#散点ax.scatter(x,y,z, s=30, c=None, depthshade=True)
#画线ax.plot(xs, ys, *args, **kwargs)
ax.plot_surface(x,y,z, rstride=1, cstride=1, cmap='rainbow')
ax.contourf(x,y,z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)
plt.show()
