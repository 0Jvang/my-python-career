def line(func):
	def deco(*argu, **kwargu):
		print('-'*30)
		retu = func(*argu, **kwargu)
		return retu
	return deco

#@line
def pnum(num1, num2):
	print(num1, num2)
	return print(num1+num2)

@line
def ptext(text):
	print(text)

pnum(1,2)
ptext('你好')
