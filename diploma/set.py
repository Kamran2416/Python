basket={'apple','banana','apple','orange','banana','pear'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a= set('abracadabra') #a set is a unique letters in string
b=set('alakazam')

print(a)
print(b)

#letters in a but not in b
print("#letters in a but not in b",a - b)

#lettters in a or b
print("letters in a or b",a | b)

#letters in a and b 
print("letters in a and b",a & b)

#letters in  a or b but not in both
print("letters in a and b but not in both ",a ^ b)
