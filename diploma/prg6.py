#WAP to accept 10 names from the user and store the name in the list only if the name has equal to or more than 6 character
word=[]
for i in range(3):
    n=input("Enter The Name:")
    if len(n) >= 6:
        word.append(n)

print(word)