import pickle
info=['王谭旭', 21]
with open('1.txt', 'wb') as f:
    pickle.dump(info, f)#序列化
with open('1.txt', 'rb') as f:
    info=pickle.load(f)#反序列化
    print(info)
