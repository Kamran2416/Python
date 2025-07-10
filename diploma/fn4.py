from random import random

def Something():
    print("Wallahi")
    if(True):
        print("Habibi")

def fun():
    a=random()* 10
    return round(a)

#Something()
rt=fun()

n=int(input("Enter a Number..."))

if( rt == n):
    print("You Won The Lottery..")
else:
    print("Better Luck Next Time...")

print("Lotter Number Is ",rt)