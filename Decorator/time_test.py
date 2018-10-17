import time
from functools import wraps

def time_test(num):
	def middle(func):
		@wraps(func)
		def wrapper(*args, **kw):
			start_time = time.clock()
			for i in range(num):
				func(*args, **kw)
			end_time = time.clock()
			print(end_time - start_time)
		return wrapper
	return middle

class time_test_class():
	"""docstring for time_test"""
	def __init__(self, num, func, *args, **kw):
		start_time = time.clock()
		for i in range(num):
			func(*args, **kw)
		end_time = time.clock()
		print(end_time - start_time)
