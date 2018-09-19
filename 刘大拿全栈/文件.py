with open(r'path', 'r|w|x|a|+ tb') as f:
    #只读
    f.read()#字符为单位
    f.readline()
    list(f)
    f.seek(offset, 0|1|2)#byte为单位
    position=f.tell()#byte为单位

    #写
    f.write()#参数只能为字符串
    f.writelines()#参数可以为list格式
