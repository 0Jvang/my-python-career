import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
y=np.sin(x)
line,= ax.plot(x,y)
def animate(i):
    line.set_data(x,np.sin(x + i/10.0))  
    return line,

def init():
    line.set_data([],[])
    return line,

ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, \
                              init_func=init,interval=20, blit=True)
plt.show()
