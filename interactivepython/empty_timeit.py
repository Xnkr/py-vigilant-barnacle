from timeit import Timer
def fn():
	pass
def test4():
    l = list(range(1000))
t4 = Timer("test4()", "from __main__ import test4")


t1 = Timer('fn()', 'from __main__ import fn')
print t4.timeit(number=1000) - t1.timeit(number=1000)