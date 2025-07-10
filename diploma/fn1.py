#function 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def findsquare(n):
    #if we give an argument then we dont need to write the below sentence
    #n=int(int(input("Enter A Number: ")))
    return n*n

i=1
while i<=10:
    print(findsquare(i))
    i+=1