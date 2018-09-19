import numpy as np
from PIL import Image
name=input()
im=np.array(Image.open(name).convert("L"))
im0=255-im #反变换
im1=im*(100/255)+150#区间变换
im2=np.power(im,2)#像素平方处理
for i in range(3):
    image=eval("{}{}".format("im",i))
    pil_im=Image.fromarray(np.uint(image))
    pil_im.show()
