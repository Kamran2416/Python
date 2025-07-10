n=int(input("Enter a number: "))
sum=0
temp=n**2
while(n!=0):
    temp = n%10
    sum = sum + temp
    n= n//10

if(temp==sum):
    print("\nneon number")
else:
    print("\nnot a neon number ")
