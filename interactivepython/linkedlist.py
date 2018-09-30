
class Node():

	def __init__(self,data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,data):
		self.data = data

	def setNext(self,next):
		self.next = next


class UnorderedList():

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,data):
		temp = Node(data)
		temp.setNext(self.head)
		self.head = temp

	def pop(self,index):
		current = self.head
		previous = None
		found = False
		if index > self.size():
			return None
		while index:
			previous = current
			current = current.getNext()
			index -= 1
		data = current.getData()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
		return data

	def insert(self,item,index):
		current = self.head
		previous = None
		found = False
		if index > self.size():
			return None
		while index:
			previous = current
			current = current.getNext()
			index -= 1
		temp = Node(item)
		if previous == None:
			self.head = temp
			temp.setNext(current)
		else:
			previous.setNext(temp)
			temp.setNext(current)

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found and current != None:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())
		else:
			return found

	def size(self):
		temp = self.head
		count = 0
		while temp != None:
			temp = temp.getNext()
			count += 1
		return count

	def search(self,data):
		temp = self.head
		found = False
		while not found and temp != None:
			if temp.getData() == data:
				return True
			else:
				temp = temp.getNext()
		return found

	def index(self,data):
		temp = self.head
		index = -1
		found = False
		while not found and temp != None:
			if temp.getData() == data:
				found = True
			else:
				temp = temp.getNext()
			index += 1
		return index if found else -1

	def append(self,data):
		temp = self.head
		while temp.getNext() != None:
			temp = temp.getNext()

		item = Node(data)
		item.setNext(temp.getNext())
		temp.setNext(item)

	def getHead(self):
		return self.head.getData()

	def __str__(self):
		temp = self.head
		st = []
		for i in range(self.size()):
			st.append(temp.getData())
			temp = temp.getNext()
		return " ".join([str(i) for i in st])


myList = UnorderedList()

# Add
for i in reversed(range(20)):
	myList.add(i)
print myList.size()

# Remove
myList.remove(50)
print myList.size()

#Search
print myList.search(49)

# Pop
print myList.pop(49)
print myList.search(49)
print myList.size()

# Insert
myList.insert(49,49)
print myList.search(49)

# Index
print myList.index(99)

#Append 
myList.append(200)
print myList.index(200)


class OrderedList(UnorderedList):

	def add(self,item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp

		else:
			temp.setNext(current)
			previous.setNext(temp)

	def search(self,item):
	    current = self.head
	    found = False
	    stop = False
	    while current != None and not found and not stop:
	        if current.getData() == item:
	            found = True
	        else:
	            if current.getData() > item:
	                stop = True
	            else:
	                current = current.getNext()

	    return found


oList = OrderedList()

for i in reversed(range(20)):
	oList.add(i)

print oList.size()

print myList
print oList