def prime_number(n):
	for i in range(2, n//2+1):
		if n//i:
			return None
	return n
