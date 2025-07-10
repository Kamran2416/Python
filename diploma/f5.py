# Function if no return value than return NONE

from ssl import OP_NO_RENEGOTIATION


def add(n1,n2):
    print("the Sum Of The Two Numbers Is: ",n1+n2)

ans=add(200,300)
print(ans)

names=["Kamran","Hassan","Irqan"]
fruits=["Apple","Banana","Kiwi","Orange"]
vegetables=["Carrot","Cucumber","LadyFinger","Pepper"]

def printlist(list):
    for i in list:
        print(i)

printlist(names)
print()
printlist(fruits)
print()
printlist(vegetables)
print()

'''
for n in names:
    print(n)

print()

for f in fruits:
   print(f)

print()

for v in vegetables:
    print(v)

print()'''
