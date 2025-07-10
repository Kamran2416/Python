list_1=["Kamran","maria","Esa"]
print(list_1)

list_1.append("Yash")
print(list_1)


print(list_1.index("maria"))
print(len(list_1))

list_2=[5,4,1,9,7]
list_2.sort()
print(list_2)

list_2.pop(4)
print(list_2)

del list_2[0]
print(list_2)

list_1.remove("maria")
print(list_1)

print("Kamran" in list_1)

print("Kamran" not in list_1)


list_3=[]

for name in range(0,4):
    name=input("Enter Your Name: ")
    list_3.append(name)

print(list_3)