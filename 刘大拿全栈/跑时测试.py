import timeit
a='''
lst=[1,2,3,4,5]
lst_new=[]
for i in lst:
    lst_new.append(i*10)
'''
b='''
lst=[1,2,3,4,5]
def f(n):
    return n*10
rst=map(f,lst)
'''
print(timeit.timeit(stmt=a,number=1000000))
print(timeit.timeit(stmt=b,number=1000000))

