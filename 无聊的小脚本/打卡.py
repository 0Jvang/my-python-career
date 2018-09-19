import time
from datetime import datetime
time1 = datetime(2018, 7, 23)
time2 = datetime.now()
words = '坚持jl和运动'
while 1:
    text = input('打卡：')
    if text==words:
        break
    else:
        print('请重新打卡')
time_ = (time2-time1).days
print('开始打卡日期：\t'+time1.strftime('%Y-%m-%d'))
print('当前日期：\t'+time2.strftime('%Y-%m-%d'))
print(f'已坚持打卡{time_}天')
with open('打卡.txt', 'a') as f:
    f.write(f'已坚持打卡{time_}天\n')
time.sleep(100)

