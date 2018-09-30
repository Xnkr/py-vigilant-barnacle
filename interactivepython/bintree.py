class BinaryTree():

	def __init__(self,root):
		self.root = root
		self.left = None
		self.right = None
		self.traverse = []

	def insertLeft(self,node):
		t = BinaryTree(node)
		if self.left == None:
			self.left = t
		else:
			x = self.left
			self.left = t
			t.left = x

	def insertRight(self,node):
		t = BinaryTree(node)
		if self.right == None:
			self.right = t
		else:
			x = self.right
			self.right = t
			t.right = x

	def getRoot(self):
		return self.root

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setRoot(self,value):
		self.root = value

	def preorder(self):
		self.traverse = []
		self.preorder_list(self.traverse)
		return self.traverse

	def preorder_list(self,t_list):
		t_list.append(self.root)
		if self.left:
			self.left.preorder_list(t_list)
		if self.right:
			self.right.preorder_list(t_list)

	def postorder(self):
		t_list = []
		self.postorder_list(t_list)
		return t_list

	def postorder_list(self,t_list):
		if self.left:
			self.left.postorder_list(t_list)
		if self.right:
			self.right.postorder_list(t_list)
		t_list.append(self.root)

	def inorder_helper(self):
		t_list = []
		self.inorder_list(t_list)
		return t_list

	def inorder_list(self,t_list):

		if self.left:
			self.left.inorder_list(t_list)
		t_list.append(self.root)
		if self.right:
			self.right.inorder_list(t_list)

	def inorder(self,t_list=[]):

		if self.left:
			self.left.inorder(t_list)
		t_list.append(self.root)
		if self.right:
			self.right.inorder(t_list)
		return t_list



if __name__ == '__main__':
	a = BinaryTree('a')
	print a.getRoot()
	print a.getLeft(), a.getRight()
	a.insertLeft('b')
	a.left.insertRight('e')
	a.insertRight('c')
	print a.getRoot()
	print a.getLeft().getRoot(), a.getRight().getRoot()

	print a.preorder()
	print a.postorder()
	print a.inorder_helper()
	print a.inorder()