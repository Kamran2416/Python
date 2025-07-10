#how to Open and Read a file 

import os


f=open("content.txt","r")
content=f.read()
#print(content)
f.close()

#how to determine how many words are there in that file
words=content.split()
print("Words In The File Are: ",len(words))


