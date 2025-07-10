#Dice Roller Simulator

import random as r

while True:
    print("1. Roll The Dice \n2.Exit\n")
    choice=int(input("Enter Your Choice: "))
    if choice ==1:
        print("Rolling The Dice\n")
        print(r.randint(1,6))
    else:
        break