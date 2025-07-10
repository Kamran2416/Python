
class Person(object):

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		self.emp1= False


class Employee(Person):
	def isEmployee(self):
		self.emp1= True
	def display(self):
		print(self.name,self.emp1)


emp = Person("Maria") 
print(emp.getName())
emp.isEmployee()

emp = Employee("Kamran")
print(emp.getName())

emp.isEmployee()
emp.display()
