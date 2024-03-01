import pandas as pd
import numpy as np

ds = pd.read_csv('C:/1-python/Python ADVANCE/Data_sets/loan.csv')
print(ds)
ds.dtypes

# x = ds.shape
# print(x)

# y = ds.size
# print(y)

# z = ds.columns
# print(z)

# s = ds.values
# print(s)

# m = ds.index
# print(m)

df = pd.DataFrame(ds)

df1 = df.drop(df.columns[6],axis= 1)
print(df1)