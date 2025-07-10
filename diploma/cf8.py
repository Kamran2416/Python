#wap to print fibonacci series upto nth term

#output: 0 1 1 2 3  5 8 13 21 34 55 89

n=int(input("Enter The Number of terms: "))
i=3
n1=0
n2=1

print(n1,n2nend=' ')
n3=n1+n2
while i<=n:
    n3=n1+n2
    print(n3,end=' ')
    n1=n2
    n2=n3
    i+=1
    
