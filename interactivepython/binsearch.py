def binsearch(a,item):
	first = 0
	last = len(a)-1
	found = False
	while first <= last and not found:
		midpoint = first + last
		midpoint /= 2
		if a[midpoint] == item:
			found = True
		if a[midpoint] > item:
			last = midpoint - 1
		else:
			first = midpoint + 1

	return found

def binarysearch(a,high,low,item):
	mid = high+low
	mid /= 2
	print a[mid]
	if a[mid] == item:
		return True
	elif high >= low:
		if a[mid] < item:
			found = binarysearch(a,high,mid + 1,item)
		else:
			found = binarysearch(a,mid - 1,low,item)
		
		return found
	else:
		return False

print binarysearch( [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] ,len( [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] ) - 1,0,16)
print binsearch(range(200),201)