students={1:"Kamran",2:"maria"}



def addContact():
    roll=int(input("Enter The Roll no: "))
    name=input("Enter The Name: ")
    students[roll]=name

def updatecontact():

    roll=int(input("Enter The Roll no You Want To Update: "))
    if roll in students:
        addContact()
    else:
        print("Invalid Number")


def searchContact():
    roll=int(input("Enter The Roll no You Want To Search: "))
    if roll in students:
        print(roll,students[roll])

def deleteContact():
    roll=int(input("Enter The Roll no You Want To Delete: "))
    if roll in students:
        del students[roll]
    else:
        print(roll,"contact not found")

def display():
    for k,v in students.items():
        print(k,v)


while True:
    print("\n\n\n1.Add\n2.Delete\n3.Search\n4.Update\n5.Display")
    user=int(input("Enter Your Choice:"))
    if user == 1:
        addContact()
    elif user == 2:
        deleteContact()
    elif user == 3:
        searchContact()
    elif user == 4:
        updatecontact()
    elif user == 5:
        display()
    else:
        break