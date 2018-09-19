from datetime import datetime
time1 = datetime(2018, 7, 17)
time2 = datetime.now()
words = '我一定能坚持j每天l和运动'
while 1:
    text = input('打卡：')
    if text==words:
        break
    else:
        print('请重新打卡')
time = (time2-time1).days
print('开始打卡日期：'+'\t'+time1.strftime('%Y-%m-%d'))
print('当前日期：'+'\t'+time2.strftime('%Y-%m-%d'))
print(f'已坚持打卡{time}天')


