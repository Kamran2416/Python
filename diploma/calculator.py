
def add(n1,n2):
    print("Ans",n1 + n2)

def sub(n1,n2):
    print("Ans",n1 - n2)

def mul(n1,n2):
    print("Ans",n1 * n2)


def div(n1,n2):
    print("Ans",n1 / n2)

def sqr(n1):
    print("Ans",n1*n1)

def mod(n1,n2):
    print("Ans",n1%n2)



num1=int(input("Enter The First Number: "))
num2=int(input("\nEnter The Second Number: "))
choice=int(input("\n0:Exit\n1:Addition\n2:Subtract\n3:Multiply\n4:Divide\n5:Mod\n6:Square\n"))
while choice!=0:
    if choice==1:
        add(num1,num2)
    elif choice==2:
        sub(num1,num2)
    elif choice==3:
        mul(num1,num2)
    elif choice==4:
        div(num1,num2)
    elif choice==5:
        mod(num1,num2)
    elif choice==6:
        num=int(input("Enter The Number For Square"))
        sqr(num)
    else:
        print("Invalid Choice")
    choice=int(input("\n0:Exit\n1:Addition\n2:Subtract\n3:Multiply\n4:Divide\n5:Mod\n6:Square\n"))




""" Create a funciton to validate if the user have score first class or not ny accepting the parameters name subjects(physcis chemistry maths) if 75 up dist
Create two function in one perform add in one perform square and call them  """