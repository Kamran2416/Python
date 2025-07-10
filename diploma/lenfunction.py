para="My Name Is Kamran Dhopaunkar"
print(len(para))

l=para.split()
print(len(l))

print(l)
u=[]
for i in l:
    if i not in u:
        u.append(i)
print(u)
