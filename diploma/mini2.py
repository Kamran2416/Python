# Random Guessing Number -MATKA
import random as r
number=r.randint(1,10)
#print(number)

for i in range (0,3):
    guess =int(input("Enter Your Guess: "))
    if guess== number:
        print("You Guessed Correct")
        print("The Number Was :",number,"\nYou Won!\n")
        break
    else:
        print("Wrong Guess")
        if i == 2:
            print("You Lost.")
            print("The Number Was : ",number)
            print("Play Again Next Time\n")
            break