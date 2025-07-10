fruits = ['banana', 'orange', 'apple', 'kiwi', 'pear', 'grapes', 'orange']
print(len(fruits))
print(fruits)
'''for f in fruits:
print(f)'''

fruits.append('mango')
print(fruits)

print(fruits.index('orange'))

print('kiwi' in fruits)

print('berries' not in fruits)

fruits.remove('orange')
print(fruits)

fruits.insert(0, 'peach')
print(fruits)

fruits.insert(3, 'peach')
print(fruits)

del fruits[0]
print(fruits)

fruits.clear()
print(fruits)