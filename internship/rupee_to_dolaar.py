e=True
temp=0
while e:
    print("\n1.Rupees to dollars\n2.Dollars to rupees\n3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        r=int(input("Enter Rupees"))
        temp= r/83.14
        print("Dollars is: ",temp)
    if choice==2:
        r=int(input("Enter Dollars"))
        temp= r*83.14
        print("Rupees is: ",temp)
    else:
        e=False
