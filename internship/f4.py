t = ("Raza", 32, ["C", "C++", "Java"])
print(type(t))
for i in t:
    print(i)
    
for i in t[2]:
    print(i)
    
t[2][0] = "Python"
print(t[2])

u = (t, "Visual Labs", 5, True)
print(u)

u[0][2][1] = "Javascript"
print(u[0])