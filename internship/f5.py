"""s={1,2,3,4,5}
s2={4,5,6,7,8}


print(s)
print(s2)

print("Difference",s.difference(s2))

print("Symetric doffernce",s.symmetric_difference(s2))
print("Union",s.union(s2))
s.add(9)
print("Add 9",s)
print("disjoint",s.isdisjoint(s2))
print(s)


"""


d1={"name":"Kamran",
    "age":19,
    "isvalid":True}
"""
for k,v in d1.items():
    print(k,v)
"""

for k in d1.keys():
    print(k)

for k in d1.values():
    print(k)

