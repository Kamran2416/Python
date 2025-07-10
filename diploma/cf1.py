# Find the greatedt of three numbers

n1=int(input("Enter The First Number: "))
n2=int(input("Enter The Second Number: "))
n3=int(input("Enter The Third Number: "))

if n1>n2:
    if  n1>n3:
        print("n1 Is Greatest")
    else:
        print("n3 Is Geratest")
else:
    if n2>n3:
        print("n2 Is Greatest")
    else:
        print("n3 Is Greatest ")