import numpy as np 
import matplotlib.pyplot as mlp
"""a0=np.array(45)
print(a0)


a1=np.array([1,2,3,4,5])
print(a1)
a2=np.array([[1,2,3],[4,5,6]])
print(a2)


a3=np.array([[[1,2,3]],[[4,5,6]]])
print(a3)

a4=np.array([[[[1,2,3]]],[[[4,5,6]]]])
print(a4)

a5=np.array([[[[[1,2,3]]]],[[[[4,5,6]]]]])
print(a5)

c=a1.copy()
print(c)
c[2]=0
print(c)
print(a1)

print(c.base)

z=a1[1:4].view()
print(z)

x=a1+a1
print(x)


print(np.concatenate((a1,x)))

print(np.split(a1,2))
"""

#////////////////////////////////////////////////////////////////////////////////////////////////
"""
x=np.array([1,2,3,4,5])

y=np.array([6,7,8,9,10])

mlp.plot(x,y,marker="o",linestyle="dashed")
mlp.show()

mlp.xlabel("X")
mlp.ylabel("Y")
mlp.bar(x,y,color="b")
mlp.show()

l=["A","B","C","D","E"]
exp=[0,0,0,0.1,0]
mlp.pie(x,labels=l,explode=exp)
mlp.legend()
mlp.show()

"""

"""
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

mlp.subplot(1, 2, 1)
mlp.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

mlp.subplot(1, 2, 2)
mlp.plot(x,y)

mlp.show()

"""

"""
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

mlp.scatter(x,y)
mlp.show()

"""

"""
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

mlp.hist(x)
mlp.show()
"""

"""
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
mlp.plot(x,y)
mlp.grid()
mlp.show()
"""