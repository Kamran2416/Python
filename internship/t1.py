import random
l1=["maria","kamran"]
choice=0
score1=0
score2=0
loop=True
while(loop):
    for i in l1:
        answer= ''.join(random.sample(i,len(i)))
    print(answer)
    choice=int(input("Enter 0 to exit 1 to continue"))
    print("The first word is ",answer)
    if choice ==1:
        s1=input("Enter The first Letter for pplayer 1")
        if s1 == answer:
            score1+=1
        else:
            answer= ''.join(random.sample(l1,len(l1)))
            print("The first word is ",answer)
            s2=input("Enter The first Letter for pplayer 2")
            if s2== answer:
                score2+=1
    else:
        loop=False
    
print(score1)
print(score2)

