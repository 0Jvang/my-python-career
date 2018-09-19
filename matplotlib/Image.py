import matplotlib.pyplot as plt,numpy as np

a=np.random.random(900).reshape(30,30)
plt.imshow(a,interpolation='nearest',cmap='bone')
plt.colorbar(shrink=0.5)
plt.xticks(())
plt.yticks(())
plt.show()
