#random Password Generator
import random as r

passlen=int(input("Enter The Length Of The Password: "))
#print("Password length: ",passlen)

optionkeys ='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
p=''.join(r.sample(optionkeys,passlen))
print('Your Password Is: ',p)





#passlen=int(input("Enter The Length Of The Password: "))
#print("Password length: ",passlen)

#optionkeys ='0123456789?'
#p=''.join(r.sample(optionkeys,passlen))
#print('Your OTP Is: ',p)