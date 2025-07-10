# function with parameter and with return value 
def add(n1,n2):
    return (n1+ n2)
print("Enter Two Numbers To add:")
num1=int(input("Enter The First Number: "))
num2=int(input("Enter The Second Number: "))
ans=add(num1,num2)
print("The Sum Of The Two Number Is: ",ans)

print("The Sum Of The Two NUmebr Is: ",add(100,300))