import turtle as t
#画布配置
t.speed(0)
#数据读取
data=[]
f=open("data.txt")
for i in f:
    i=i.replace("\n"," ")
    data.append(list(map(eval,i.split(","))))
f.close
print(data)
#自动绘制
for i in range(len(data)):
    t.fd(data[i][0])
    if data[i][1]:
        t.left(data[i][2])
    else:
        t.right(data[i][2])
t.done()
    
