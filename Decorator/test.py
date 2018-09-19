from time_test import time_test

iterator = range(10**7)
generator = (i for i in range(10**7))

@time_test(0)
def f1():
	c = 0	
	for i in iterator:
		c += 1

@time_test(0)
def f2():
	c = 0;b=0
	for j in range(2):
		for i in generator:
			c += 1
		print(c)
	
# f1()
f2()
