#function with zero ,one,more parameters
def add(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    return sum

ans= add(93,144,7654,89)
print(ans)



#function with one parameter
def addlist(list):
    sum=0
    for l in list:
        sum=sum+l 
    return sum

numbers=[5,1,7,9,3]
ans2=addlist(numbers)
print(ans2)