n=int(input("Enter a number: "))
sum=0
temp=n
flag=1
while(n!=0):
    if(temp%10!=n%10):
        flag=0
        break
    n//=10
    temp//=10

if (flag==0):
    print("Auto morphic")
else:
    print("Not a autmorphic")