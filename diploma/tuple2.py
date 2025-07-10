#if we dont declare any brackets the interpreter will automatically consider as a tuple
t = 1, 2, 3 
print(t)

b=t+(4,5,6)
print(b)

v=(b,7,8,9)
print(v)

z=(t,b)
print(z)

#tuple can also have list as an element
a=(1,"Kamran",3.14,1)
print(a)

u=(True,[100,200,300],3.14)
print(u)

u[1][0]="Hundered"
print(u)