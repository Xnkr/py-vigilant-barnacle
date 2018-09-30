n = 1022
k = 2
count = len(str(n))-str(n).find(str(k))-1 if str(n).find(str(k)) != -1 else -1
if count != -1:
	print (n/(10**count))*(10**count) -1 
else: 
	print n
