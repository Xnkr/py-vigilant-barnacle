def selectionsort_maxtomin(a):
	for slot_to_fill in range(len(a)-1,0,-1):
		positionofmax = slot_to_fill

		for i in range(slot_to_fill):
			if a[i] > a[positionofmax]:
				positionofmax = i

		a[slot_to_fill], a[positionofmax] = a[positionofmax], a[slot_to_fill]
	return a

def selectionsort_mintomax(a):

	for slot_to_fill in range(0,len(a)):
		position_of_min = slot_to_fill
		for i in range(slot_to_fill+1,len(a)):
			if a[i] < a[position_of_min]:
				position_of_min = i
		a[slot_to_fill], a[position_of_min] = a[position_of_min], a[slot_to_fill]

	return a


print selectionsort_mintomax(range(3,0,-1))