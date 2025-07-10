ls=[1,2,3,4,5]
print(ls)

for i in ls:
    print(i)

print(type(ls))

ls.append(20)
print(ls)
ls.insert(0,0)
ls.remove(4)
ls.pop()
print(ls)
vl=ls.copy()

if 5 in ls:
    print("5 is there in ls")

if 5 not in ls:
    print("5 is not htere")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
new=["Kamran",42,True]
print(new)

matrix=[[1,2,3],[4,5,6],[7,8,9]]

for i in matrix:
    for j in i:
        print(j)



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

name="Kamran"
print(name)
print(name[1])

students=["kamran","hassan","irqan"]
students[2]="fehmiya"
print(students)
#students[2][1]='F' immutable

