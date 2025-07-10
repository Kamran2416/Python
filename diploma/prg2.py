#wap to store the square of first n natural number in a list
#later remove the square of 6 from the list and then print the list 

sq=[]

for i in range(1,11):
    sq.append(i**2)

print(sq)
del sq[5]