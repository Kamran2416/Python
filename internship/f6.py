import contactbook as ct 

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
        ct.add(sr,n,nu,a)
        print("added")
    elif ch==2:
        sr=int(input("enter sr no: "))
        ct.delete(sr)
    elif ch==3:
        sr=int(input("enter sr no: "))
        n=input("enter name: ")
        nu=int(input("enter numer: "))
        a=int(input("enter age: "))
        ct.update(sr,n,nu,a)
    elif ch==4:
        sr=int(input("enter sr no "))
        ct.search(sr)
    elif ch==5:
        ct.display()
    elif ch==6:
        sr=int(input("enter sr no "))
        ct.favourite(sr)
    elif ch==7:
        ct.favd()
    elif ch==8:
        break
    else:
        print("inavlid input")
"""

#/////////////////////////////////////////////////////////////////////////////////////////////
    
for i in range(1,11):
    print(i,end='\r')