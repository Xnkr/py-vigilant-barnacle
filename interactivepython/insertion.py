def insertionsort(a):

	for i in range(1,len(a)):
		curr_item = a[i]
		curr_position = i

		while curr_position > 0 and a[curr_position - 1] > curr_item:
			a[curr_position] = a[curr_position - 1]
			curr_position -= 1

		a[curr_position] = curr_item

	return a


print insertionsort(range(10,0,-1))