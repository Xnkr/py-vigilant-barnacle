def solve(n, s, d, m):
	count = 0
	for i in range(len(s)-m+1):
		if sum(s[i:i+m]) == d:
			count += 1
	return count

n = int("5".strip())
s = map(int, "1 1 1 1 1".strip().split(' '))
d, m = "3 2".strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print result