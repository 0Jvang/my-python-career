import numpy as np
a=np.array([1,1,1])[:,np.newaxis]
b=np.array([2,2,2])[:,np.newaxis]
c=np.vstack((a,b))
print(c)
c=np.hstack((a,b,b))
print(c)
c=np.concatenate((a,b,b,a),axis=0)
print(c)

