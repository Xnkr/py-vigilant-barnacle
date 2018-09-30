def quicksort(alist,first,last):

	if first < last:

		split = partition(alist,first,last)

		quicksort(alist,first,split-1)
		quicksort(alist,split+1,last)
	return alist

def partition(a,first,last):

	pivot = first
	leftmark = pivot+1
	rightmark = last

	while True:

		while leftmark <= rightmark and a[leftmark] <= a[pivot]:
			leftmark += 1

		while leftmark <= rightmark and a[rightmark] >= a[pivot]:
			rightmark -= 1 

		if rightmark < leftmark:
			break
		else:
			a[leftmark], a[rightmark] = a[rightmark], a[leftmark]

	a[pivot], a[rightmark] = a[rightmark], a[pivot]

	return rightmark

def median(l):
	return sorted(l)[(0+len(l))//2]

def partition_median(a,first,last):


	leftmark = first+1
	rightmark = last
	pivot_value = median([a[first],a[last],median(a)])

	while True:

		while leftmark <= rightmark and a[leftmark] <= a[pivot]:
			leftmark += 1

		while leftmark <= rightmark and a[rightmark] >= a[pivot]:
			rightmark -= 1 

		if rightmark < leftmark:
			break
		else:
			a[leftmark], a[rightmark] = a[rightmark], a[leftmark]

	a[pivot], a[rightmark] = a[rightmark], a[pivot]

	return rightmark


print quicksort([3,4,1,2],0,3)

a = [1,10,3,4,5,6,7]
first = 0
last = len(a)-1
print median(a)
print median([a[first],a[last],median(a)])