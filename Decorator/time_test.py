import timeit

def time_test(num):
	def middle(func):
		def wrapper(*args, **kw):
			func()
			runtime = timeit.timeit(func, number=num)
			print(runtime)
		return wrapper
	return middle