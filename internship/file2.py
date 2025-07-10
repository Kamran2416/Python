import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
df=pd.read_excel("C:\\Users\\kdhop\\OneDrive\\Desktop\\Python\\internship\\Book1.xlsx")
print(df)

plt.ylim(0,100)
plt.yticks(np.arange(0, 100, 10))
plt.bar(df['Age'],df[''])
plt.show()
