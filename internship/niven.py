n=int(input("Enter a number: "))
sum=0
temp=n
num=0
while(temp!=0):
    num = temp%10
    sum = sum + num
    temp= temp//10

if(n%sum==0):
    print("\nniven number")
else:
    print("\nnot a neven number ")
