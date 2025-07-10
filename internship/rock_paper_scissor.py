import random as rd
chance=5
co=0
us=0



while chance>0:
    coms=rd.choice(["R","P","S"])
    user=input("Enter Your Choice\n1. R for Rock \n2. S for Scissor \n3. P for Paper\n")
    if user==coms:
        print("Its a tie")
    elif user=="R":
        if coms=="P":
            print("Better luck next time")
            print("Computer chose: ",coms)
            co+=1
            
        else:
            print("You won!!!!!!!!!!!")
            us+=1
            
    elif user =="P":
        if coms=="S":
            print("Better luck next time")
            print("Computer chose: ",coms)
            co+=1
        else:
            print("You won!!!!!!!!!!!!")
            us+=1
    elif user =="S":
        if coms=="R":
            print("Better luck next time")
            print("Computer chose: ",coms)
            co+=1
        else:
            print("You won!!!!!!!!!!!!")
            us+=1
    else:
        print("Invalid Input")
    chance-=1


print("Your score is: ",us)
print("Compuetrs Score is: ",co)