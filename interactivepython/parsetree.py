from bintree import BinaryTree
from stackds import Stack

eq = '(3+(4*5))'

def parseTree(eq):
	op_list = ['+','-','*','/']

	eq_list = list(eq)
	cStack = Stack()

	eTree = BinaryTree('')
	cStack.push(eTree)
	cTree = eTree
	for i in eq_list:
		if i == '(':
			cTree.insertLeft('')
			cStack.push(cTree)
			cTree = cTree.getLeft()

		elif i == ')':
			cTree = cStack.pop()

		elif i not in op_list:
			cTree.setRoot(int(i))
			cTree = cStack.pop()

		elif i in op_list:
			cTree.setRoot(i)
			cTree.insertRight('')
			cStack.push(cTree)
			cTree = cTree.getRight()

		

		else:
			raise ValueError
	return eTree

def evaluate(parseTree):

	oper = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__floordiv__}

	left = parseTree.getLeft()
	right = parseTree.getRight()

	if left and right:
		fn = oper[parseTree.getRoot()]
		return fn(evaluate(left), evaluate(right))
	else:
		return parseTree.getRoot()

eTree = parseTree(eq)
print eTree.inorder()
print evaluate(eTree)


