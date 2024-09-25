import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("chemistry.csv")
#print(df)
#print(df.tail())
x=df.tail().iloc[:,1]
y=df.tail().iloc[:,2]
'''print(x)
print(y)
print(df.isnull().sum())'''


plt.bar(x,y)
plt.show()
