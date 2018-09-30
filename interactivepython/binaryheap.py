
class Heap():

	def __init__(self):
		self.heap = [0]
		self.size = 0

	def insert(self,item):
		self.heap.append(item)
		self.size += 1
		self.percUp(self.size)

	def percUp(self,i):

		while i//2 > 0:
			if self.heap[i] < self.heap[i//2]:
				self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]

			i //= 2

	def delMin(self):
		

a = Heap()
a.insert(10)
print a.heap
a.insert(1)
print a.heap