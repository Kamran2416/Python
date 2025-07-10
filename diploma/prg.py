#write A program to accept 5 name from the user and store it in a list  
#later if aimna is there in those 5 students 

#a= input("Enter The name of the first student: ")
#b= input("Enter The name of the first student: ")
#c= input("Enter The name of the first student: ")
#d= input("Enter The name of the first student: ")
#e= input("Enter The name of the first student: ")
#student =[a,b,c,d,e]
#print(student)
#print('Aiman' in student)
name=[]
for i in range (5):
    str=input("Enter The Name: ")
    name.append(str)

print(name)

print("Is Aiman on the list: ", 'aiman' in name)

