# multiple inheritance

class A(object):
	def __init__(self):
		self.str1 = "Kamran"
		print("Claas A")


class B(object):
	def __init__(self):
		self.str2 = "Maria"
		print("Class B")


class Derived(A, B):
	def __init__(self):
		A.__init__(self)
		B.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
