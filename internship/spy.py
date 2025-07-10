n=int(input("Enter a number: "))
sum=0
temp=n
num=0
p=1
while(temp!=0):
    num = temp%10
    sum = sum + num
    p=p*num
    temp= temp//10

if(sum==p):
    print("spy number")
else:
    print("not a spy numer")