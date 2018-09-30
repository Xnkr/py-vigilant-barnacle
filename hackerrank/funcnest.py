def writer():
	title = 'Sir'
	name = (lambda x:title + ' ' + x)
	return name

who = writer()
print(who('Arthur'))

def sum1(*args):
	r = 0
	for i in args:
		r += i
	return r

print sum1(1,2,3)
print sum1(1,2,3,4,5)