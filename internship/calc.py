
def Add(num1,num2):
    return num1 + num2

def Subtract(num1,num2):
    return num1 - num2

def Multiply(num1,num2):
    return num1 * num2

def Divide(num1,num2):
    return num1 // num2

while True:
    print("Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(Add(num1, num2))
        
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(Subtract(num1, num2))
        
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(Multiply(num1, num2))
    
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(Divide(num1, num2))
        
    elif choice == 5:
        break
    
    else:
        print("Invalid choice")