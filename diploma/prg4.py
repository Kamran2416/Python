#WAp to accept list of numbers from the user and display only odd numbes from the list
no=[]
for i in range(5):
    n=int(input("Enter a number: "))
    no.append(n)
print(no)

for i in range(5):
       if no[i]%2 ==0:
           print(no[i])
