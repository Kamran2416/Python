contacts={1:{"name":"kamran","number":9820284802,"age":19},
          2:{"name":"hassan","number":1234567890,"age":19},
          3:{"name":"irqan","number":9876543223,"age":19}}
fav={}
def add(sr,n,nu,a):
    if sr in contacts:
        print("value already exist so updated")
        update(sr,n,nu,a)
    else:
        contacts[sr]={"name":n,"number":nu,"age":a}

def delete(sr):
    if sr not in contacts:
        print("value not found")
    else:
        del(contacts[sr])
        print("deleted")

def update(sr,n,nu,a):
    if sr in contacts:
        print("new value")
        add(sr,n,nu,a)
    else:
        contacts[sr]={"name":n,"number":nu,"age":a}
        print("updated")

def search(sr):
    if sr in contacts:
        print("contact is ",contacts[sr]["name"]," ",contacts[sr]["number"]," ",contacts[sr]["age"])
    else:
        print("not found")

def display():
        for k,v in contacts.items():
            print("---------------------------------------------------------------------------------------")
            print("Contact details")
            for key,val in v.items():
                print(key,"->",val)
            

def favourite(sr):
    if sr in contacts:
        fav[sr]=contacts[sr]

def favd():
    for k,v in fav.items():
            for key,val in v.items():
                print(key,"->",val)

"""while(True):
    print("\n1. ADD")
    print("\n2. DELETE")
    print("\n3. UPDATE")
    print("\n4. SEACRH")
    print("\n5. DISPLAY")
    print("\n6. FAV CONNTACT")
    print("\n7. FAV DISPLAY")
    print("\n8. EXIT")
    ch=int(input("\nEnter your choice: "))
    if ch==1:
        sr=int(input("enter sr no: "))
        n=input("enter name: ")
        nu=int(input("enter numer: "))
        a=int(input("enter age: "))
        add(sr,n,nu,a)
        print("added")
    elif ch==2:
        sr=int(input("enter sr no: "))
        delete(sr)
    elif ch==3:
        sr=int(input("enter sr no: "))
        n=input("enter name: ")
        nu=int(input("enter numer: "))
        a=int(input("enter age: "))
        update(sr,n,nu,a)
    elif ch==4:
        sr=int(input("enter sr no "))
        search(sr)
    elif ch==5:
        display()
    elif ch==6:
        sr=int(input("enter sr no "))
        favourite(sr)
    elif ch==7:
        favd()
    elif ch==8:
        break
    else:
        print("inavlid input")


"""