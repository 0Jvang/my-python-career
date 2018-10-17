from time_test import time_test, time_test_class

lst1 = [3,7,8,9,12]
lst2 = [5,6,10,13,25,30]

@time_test(100000)
def f1():
    lst = lst1 + lst2
    le = len(lst)-1
    for i in range(le):
        for j in range(le):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    # print(lst)

@time_test(100000)
def f2():
    for i in lst1:
        for j in range(len(lst2)):
            if i < lst2[j]:
                lst2.insert(j, i)
                break
    # print(lst2)

f1()
f2()


