#panda used for data analysis 
# used to read access data that is in tabular format
# read the file in the form of csv hdfs(hadoop distributed file sysytem)
# stands for Panel data and data analysis
# Series(one row) anda data frame()

import pandas as pd
"""
x=pd.Series(["name","address","age"] ,index=["A","B","C"])
print(x)
"""
""""
y= pd.DataFrame({"name":["Kamran","Hassan","Irqan"],
                 "age":[20,19,18],
                 "addd":["mazgaon","bycualla","parel"]})

print(y)

y["name1"]=["Hasina","Fehmiya","sarah"]
print(y)
print("######################################")
print(y["age"].max())
print(y["age"].min())
print(y["age"].describe())"""

x=pd.read_csv("data.csv")
print(x)










