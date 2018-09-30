def shellsort(alist):

	sublist_size = len(alist)/2

	while sublist_size > 0:

		for start_pos in range(sublist_size):

			gap_insertion_sort(alist, start_pos, sublist_size)

		sublist_size /= 2


	return alist

def gap_insertion_sort(alist, start_pos, gap):
# Because first element is considered to be sorted in insertion sort
	for i in range(start_pos+gap, len(alist), gap ):

		current_item = alist[i]
		position = i

		while position >= gap and alist[position-gap] > current_item:
			alist[position] = alist[position - gap]

			position -= gap

		alist[position] = current_item

import numpy as np

randomlist = np.random.randn(10).tolist()
print shellsort(randomlist)

print shellsort(range(10,0,-1))