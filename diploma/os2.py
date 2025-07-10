#how to open and write in a file 
import os

str=input("Enter A Sentence: ")
print(str)

#if we write w in the second argument it will only wite the new sentence and dlete the old sentence 
#if we write a in the second argument it will add the new sentence in the existing sentence
f=open("pontent.txt",'a')

for s in str:
    f.write(s)

#to add a space in the sentence if we use a argument
f.write(' ')

f.close()
