students=["Kamran","Hassan","Irqan"]
fruits=["Apple","Banana","Cherry"]
vegetables=["Carrot","Cucumber","Eggplant"]
languages=["Python","C","C++","Java"]

def printlist(list):
    for items in list:
        print(items,end=' ')


print("\nStudents: ",end=' ')
printlist(students)

print("\nFruits: ",end=' ')
printlist(fruits)

print("\nVegetables: ",end=' ')
printlist(vegetables)

print("\nLanguages: ",end=' ')
printlist(languages)