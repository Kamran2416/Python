#wap to print a list of containing factorials of first 10 numbers 
l=[]


def factorials(n):
    fact=l
    for i in range(1,n+1):
        fact=fact+1
    return fact


#print(factorials)

for i in range(1,6):
    l.append(factorials(i))

print(l)