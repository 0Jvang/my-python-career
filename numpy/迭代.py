import numpy as np
a=np.arange(9).reshape((3,3))
for i in a:#迭代行
    print(i)
for i in a.T:#迭代列
    print(i)
for i in a.flatten():#迭代每个元素
    print(i)


