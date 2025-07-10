print('Enter 8 Elements of Dataset: ')
data = list()

# getting data
for i in range(0, 8):
    n = int(input())
    data.append(n)
    
# function to create clusters based on means
def calcluster(m1, m2, k1, k2):
    k1.clear()
    k2.clear()
    for n in data:
        #print(abs(m1-n), '<', abs(m2-n))
        if abs(m1-n) < abs(m2-n):
            k1.append(n)
        else:
            k2.append(n)
    # print("\n", m1, k1, m2, k2, "\n")

# selecting random means
m1 = data[4]
m2 = data[1]

# initializing lists
k1 = list()
k2 = list()

tempM1 = -1
tempM2 = -1

# looping till same value of m1 and m2 repeats
while(True):
    calcluster(m1, m2, k1, k2)
    m1 = sum(k1)/len(k1)
    m2 = sum(k2)/len(k2)
    #print('\n', m1, tempM1, m2, tempM2, '\n')
    if tempM1 == m1 and tempM2 == m2:
        break
    tempM1 = m1
    tempM2 = m2

print(f'{m1}: {k1}, {m2}: {k2}')