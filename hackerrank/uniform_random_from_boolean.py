import random

def A():
	return bool(random.getrandbits(1))

def B():
	high = 2
	low = 0
	r = high - low + 1
	rand = A() % r + low
	return rand

print(B())

