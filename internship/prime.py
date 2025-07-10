n=int(input("enter  a number: "))
flag=1
for i in range(2,n):
    if(n%i)==0:
        flag=0
        break

if(flag==1):
    print("it is a prime number")
else:
    print("it is not a prime number")