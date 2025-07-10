#how to Open and Read a file 

import os


f=open("content.txt","r")
content=f.read()
#print(content)
f.close()

#how to determine how many words are there in that file
words=content.split()
print("Words In The File Are: ",len(words))


#to check if the word starts with an a or A
WordStartingWithA = []

for w in words:
    if w[0]=='a' or w[0] == 'A':
        if w not in WordStartingWithA:
            WordStartingWithA.append(w)

print("Words Starting With A are: ",WordStartingWithA)









# to check if your essay is longer than 250 words
'''
if len(words) < 250:
    print("Your Essay Is disqualified ")
else:
    print("Your Essay is Qualified ")
'''