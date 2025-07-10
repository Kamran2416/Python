def fact(n):
    fact=1
    for i  in range(1,n+1):
        fact=fact*i

    return fact
n=int(input("Enter a number: "))
sum=0
temp=n
num=0
f=0
while(temp!=0):
    num = temp%10
    f=fact(num)
    sum= sum + f
    temp= temp//10

if(n == sum):
    print("\nspecial numer number")
else:
    print("\nnot a special number ")


