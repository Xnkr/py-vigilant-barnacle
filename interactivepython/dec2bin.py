from stackds import Stack

def dec2bin(dec):

	rem_stack = Stack()

	while dec > 0:
		rem_stack.push(dec % 2)
		dec /= 2

	bi = []

	while not rem_stack.isEmpty():
		bi.append(str(rem_stack.pop()))

	return "".join(bi)

def dec2base(dec,base):

	digits = "0123456789ABCDEF"

	rem_stack = Stack()

	while dec > 0:
		rem_stack.push(dec % base)
		dec /=  base

	bi = []

	while not rem_stack.isEmpty():
		bi.append(digits[rem_stack.pop()])

	return "".join(bi)

print dec2base(25,8)