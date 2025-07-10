#find the avg of  p.c.m marks of a student  an determine their grade

a=int(input("Enter The Marks Of Physics:"))
b=int(input("Enter The Marks Of Chemistry:"))
c=int(input("Enter The Makrs Of Maths:"))

avg=(a+b+c)/3
print(avg)

if avg>=75:
    print("Grade A")
elif avg>=65:
    print("Grade B")
elif avg>=55:
    print("Grade C")
elif avg>=35:
    print("Grade D")
else:
    print("Grade E ~~~~~~FAIL")
