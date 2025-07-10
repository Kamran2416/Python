#reverse a list of name given by user

name=[]
for i in range(3):
    str=input("Enter The name:")
    name.append(str)
print(name)
name.reverse()
print(name)