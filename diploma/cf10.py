#wap to print list containing factorials of first 10 numbers

from re import L


l=[]

for i in range(1,10):
    fact=l 
    for j in  range (1,i+1):
        fact=fact+j
    l.append(fact)

print(l)

#############################################################################

#l=[]
#fact=1

#  for i in range(1,6):
#       fact=fact*i
#       l.append(fact)



#       print(l)