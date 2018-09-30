class HashTable():

	def __init__(self):
		self.size = 11
		self.slots = [None]*self.size
		self.data = [None]*self.size

	def hashfunction(self, key, size):
		return key%size

	def rehash(self,oldhash,size):
		return (oldhash+1)%size

	def put(self,key,data):
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data
			else:
				nextslot = rehash(hashvalue,len(self.slots))

				while self.slots[nextslot] not in [None, key]:
					nextslot = rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == key:
					self.data[nextslot] = data

				else:
					self.slots[nextslot] = key
					self.data[nextslot] = data

	def get(self,key):
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == key:
			return self.data[hashvalue]

		else:
			if self.slots[hashvalue] == None:
				return None

			else:
				nextslot = rehash(hashvalue,len(self.slots))

				while self.slots[nextslot] not in [None, key]:
					nextslot = rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == key:
					return self.data[nextslot]
				else:
					return None

	def __setitem__(self,key,data):
		self.put(key,data)

	def __getitem__(self,key):
		return self.get(key)
		

h = HashTable()

h[54] = "cat"

print h[54]
print h.slots
print h.data