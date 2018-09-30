a = "hackerrank"
b = "haaker"

def LCS(a,b,n,m):
	if n == 0 or m == 0:
		result = 0
	elif a[n-1] == b[m-1]:
		result = 1 + LCS(a,b,n-1,m-1)
	elif a[n-1] != b[m-1]:
		t1 = LCS(a,b,n-1,m)
		t2 = LCS(a,b,n,m-1)
		result = max(t1,t2)
	return result

print LCS(a,b,len(a),len(b))