def fibonacci(n):
    f = 0
    s = 1
    print(f)
    print(s)
    next = f + s
    for i in range(2 , n):
        f = s
        s = next
        next = f + s
        print(next)
        
fibonacci(50)