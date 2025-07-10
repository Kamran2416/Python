arr=[5,1,7,9,3]
print(arr)

arr.sort()
print(arr)

search=int(input("Enter The Element To be searched: "))
b=0
for i in arr:
    b+=1
    if search == i :
        print("element Found At",b)
    
