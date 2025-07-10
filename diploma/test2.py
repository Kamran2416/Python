import random as r

passlength=int(input("Enter The Number Of Passlength:"))

optionkey='a b c d e f g h i j k l m n o p q r s t u v w x y z'

password=''.join(r.sample(optionkey,passlength))
print(password)