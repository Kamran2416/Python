"""def list():
    l = []
    for i in range(1, 6):
        n = int(input(f"Enter {i} elements in list: "))
        l.append(n)
    print(l)
    print(l[: : -1])
list()"""

"""
def list():
    l=[1,2,3,4,5,6,7]
    n=[]
    for i in range(l,len(l)+1):
        print(-i)
        n.append(i)
    print(n)

list()"""


l=[1,2,3,4,5]
n=[]
i=4
while i>=0:
    n.append(l[i])
    i-=1
print(n)