import itertools
data = [chr(i) for i in range(97, 123)]
data_tuple = itertools.permutations(data, 4)
url = ['www.' + ''.join(i) + '.com' for i in data_tuple]
print(url)