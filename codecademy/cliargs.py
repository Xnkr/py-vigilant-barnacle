import sys
# print type(sys.argv[1])

l = [1 , 1]
print l

for idx,item in enumerate(l):
	if item == 1:
		l[idx] = "String 1"

print l
