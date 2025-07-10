import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
df=pd.read_csv("data.csv")
print(df.to_string())
plt.ylim(0,100)
plt.yticks(np.arange(0, 100, 10))
plt.bar(df["Name"],df["Marks"])
plt.show()


# data=pd.read_csv("data.csv")
# df = pd.DataFrame(data)
# print(df.to_string())
# plt.bar(df["Name"],df["Marks"])
# plt.show()