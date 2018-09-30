doors = [False] * 100

for i in range(1,101):
	for j in range(len(doors)):
		if (j+1)%i == 0:
			doors[j] = not doors[j]

print [i+1 for i,t in enumerate(doors) if t]