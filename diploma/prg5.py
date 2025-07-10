#wap to accept word from user only if word start from "a"

word=[]

for i in range(10):
    str=input("Enetr The name: ")
    if (str[0]=="a" or str[0]=="A"):
        word.append(str)
print(word)