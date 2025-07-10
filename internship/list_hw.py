'''ls=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in ls:
    for j in i:
        sum=sum+j

print(sum)
'''
def armstromg(n):
    final=n
    temp=0
    sum=0
    while(n>0):
        temp=n%10
        sum=sum+temp**3
        n=n//10
    
    if (sum == final):
        return 1
    else:
        return 0


ls=[19,36,79,145,153]


for i in ls:
    result = armstromg(i)
    if(result==1):
        print("In th list the number",i ," is armstrong number")