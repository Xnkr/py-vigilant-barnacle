a = "banana"
def f(a):
	strs = []
	print(len(a))
	for i in range(len(a)):
		for j in range(i,len(a)+1):
			print(i,j,a[i:j])
			if a[i:j] != "":
				strs.append(a[i:j]) 

	return strs