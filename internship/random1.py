import random as rd 

c=rd.randint(1,20)

print("Enter Your name")
name=input()
print("Ok ",name," lets start")

chance=5

while(chance>0):
    choice=int(input("Enter your guess: "))
    if choice>c:
        chance-=1
        print("\nyour guess is high")
    elif choice<c:
        chance-=1
        print("\nyour guess is lower")
    elif choice ==c:
        print("\nyour guess is correct ")
        print("\nYOU WON")
        break
    else:
        break

if chance ==0:
    print("\nthe number was",c)
    print("\nYOU LOST BETTER LUCK NEXT TIME ")
        
