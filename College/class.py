
class Student():
    def __init__(self,name,age):
        print("Constructor is called....")
        self.name=name
        self.age=age

    def sal(self,salary):
        self.sal=salary

    def lname(self,lname):
        self.lname=lname
    def display(self):
        print("Name: ",self.name,self.lname," \nAge: ",self.age," \nSalary:",self.sal)
    
    


maria=Student("Maria",37)
kamran=Student("Kamran",17)


maria.lname("Ansari")
kamran.lname("Dhopaunkar")
maria.sal(1000)
kamran.sal(1000)
maria.display()
kamran.display()
