from stackds import Stack

def revstring(mystr):
	s = Stack()

	for i in mystr:
		s.push(i)

	rev = []

	while not s.isEmpty():
		rev.append(s.pop())

	return "".join(rev)


print revstring("abcd")

