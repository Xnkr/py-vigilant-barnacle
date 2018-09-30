
def bubblesort(a):
	num_iter = len(a)-1

	for passes in range(num_iter,0,-1):
		for i in range(passes):
			if a[i] > a[i+1]:
				temp = a[i]
				a[i] = a[i+1]
				a[i+1] = temp

	return a

def shortbubble(a):
	exchange = True
	num_iter = len(a)-1

	while num_iter > 0 and exchange:
		exchange = False
		for i in range(num_iter):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
				exchange = True
		num_iter -= 1

	return a

print shortbubble(range(10,0,-1))