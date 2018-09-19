import matplotlib.pyplot as plt
plt.figure()
ax1=plt.subplot()
ax2=ax1.twin()
ax2.set_ylim(0,5)
plt.show()
