contact={"Kamran":1234567890,"Hassan":6536547890,"Irqan":9489767296}


def add_con(name,number):
    contact[name]=number

def del_con(name):
    if name in contact:
        del contact[name]
    else:
        print("Not existing")

def update_con(name,number):
    contact[name]=number

def search_con(name):
    if name in contact:
        print("Name ", name ," Is Present")
    else:
        print("Name ", name ," Is Not Present")

def display():
    for k,v in contact.items():
        print(k,v)



print("\nCONTACT LIST\n")
print("1. Add")
print("2. Delete")
print("3. Update")
print("4. Search")
print("5. Dsiplay")
print("6. Exit\n")

choice=int(input("Enter your Choice: "))


while(choice != 6):
    if choice == 1:
        name=input("Enter the Name To add: ")
        number=int(input("Enter The Number To add: "))
        add_con(name,number)
        display()
    elif choice == 2:
        name=input("Enter the Name To Delete: ")
        del_con(name)
        display()
    elif choice == 3:
        name=input("Enter the Name To Update: ")
        number=int(input("Enter The Number To Update: "))
        add_con(name,number)
        display()
    elif choice == 4:
        name=input("Enter the Name To Search: ")
        search_con(name)
    elif choice == 5:
        display()
    else:
        print("Invalid Input")

    print("\nCONTACT LIST\n")
    print("1. Add")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Dsiplay")
    print("6. Exit\n")
    choice=int(input("Enter your Choice: "))
    