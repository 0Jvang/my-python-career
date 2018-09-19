import re
bookname=input('请输入书名：')
name1=input('请输入人物名：')
name2=input('请输入人物名：')
text=open(bookname+'.txt','r',encoding='utf-8').read()
pattern=re.compile(r'({}|{})([^”]*”)'.format(name1,name2))
results = pattern.findall(text)
for i, r in enumerate(results[1500:1600], 1):
    print(i, ''.join(r))
