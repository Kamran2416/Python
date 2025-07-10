def list():
    l = []
    sum = 0
    for i in range(1, 6):
        n = int(input(f"Enter {i} elements in list: "))
        l.append(n)
        sum = sum + n
    print(l)
    print(sum)
        
list()