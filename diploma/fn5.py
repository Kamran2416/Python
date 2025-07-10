def add(a,b):
    print(a+b)

def addNumbers(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n

    return sum

#add(1,1)
#add("1","1")
#add([1,2,3],[4,5,6])
#add((1,2,3),(4,5,6))

ans=addNumbers(1,2,3)
print(ans)