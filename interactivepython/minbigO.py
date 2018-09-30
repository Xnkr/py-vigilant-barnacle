import time

def func1(n):
	minn = 0
	start = time.time()
	for i in range(len(n)):
		minn = n[i]
		for j in range(len(n)):
			if n[j] < minn:
				minn = n[j]
	end = time.time()
	return minn, end-start



def func2(n):
	minn = n[0]
	start = time.time()
	for i in n:
		if i < minn:
			minn = i
	end = time.time()
	return minn, end-start

n = range(100000,0,-1)
print func1(n),func2(n)