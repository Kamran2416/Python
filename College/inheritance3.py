#multilevel inheritance

class Mother:
	mothername = ""

	def mother(self):
		print(self.mothername)

class Father:
	fathername = ""

	def father(self):
		print(self.fathername)

class Daughter(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)

s1 = Daughter()
s1.fathername = "Imran"
s1.mothername = "Gulrukh"
s1.parents()
