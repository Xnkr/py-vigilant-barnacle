class Stack():

	def __init__(self):
		self.stack = []

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[len(self.stack)-1]

	def isEmpty(self):
		return True if len(self.stack) == 0 else False

