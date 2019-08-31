i = 1
number = 10000019
list_palindromes = []
element = number * i
while element < (10**14):
	e = str(element)
	for j in range(len(e)):
		if e[j] != e[len(e)-j-1]:
			break
		if len(e)-1 == j:
			list_palindromes.append(e)
			print(e)
	i += 1
	element = number * i