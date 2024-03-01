import pandas as pd
import numpy as np

data = {
               'Coursera':['cyber security', 'AL and ML', 'DSA','spark','pyspark'],
               'fee': [2000,2500,260000,4600,1234],
               'duration': ['30days','40days','35days','90days','15days']
            }

row = ['r1','r2','r3','r4','r5']
df = pd.DataFrame(data , index = row)

# delete the 3rd index row in dataframe 
df1 = df.drop(df.index[3])
print(df1)

# deletes the rows whos index mentioned (for that use '[[]]')
df2 = df.drop(df.index[[2,4]])
print(df2)

df3 = df.drop('r1')
print(df3)

df4 = df.drop(['fee'],axis=1)
print(df4)

print(df.drop(df.columns[0],axis = 1))
# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
import numpy as np

data = {
               'Coursera':['cyber security', 'AL and ML', 'DSA','spark','pyspark'],
               'fee': [2000,2500,260000,4600,1234],
               'duration': ['30days','40days','35days','90days','15days']
            }

row = ['r1','r2','r3','r4','r5']
df = pd.DataFrame(data , index = row)

liscol = ['Coursera','fee']
df2 = df.drop(liscol, axis=1) 
print(df2)

# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
# import numpy as np 

data = {
               'Coursera':['cyber security', 'AL and ML', 'DSA','spark','pyspark','propmt','ui & ux','sql'],
               'fee': [2000,2500,260000,4600,1234,2000,5000,6000],
               'duration': ['30days','40days','35days','90days','15days','7days','9days','10days']
            }

row = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(data , index = row)
df2 = df.iloc[:,::2]
print(df2)

df2 = df.iloc[:,0:1]
print(df2)

df3 = df.iloc[0:2,:]
print(df3)

D = df.iloc[2]
print(D)

df2 = df.iloc[[2,3,6]]
print(df2)

print(df)
dx = df.iloc[-1:,-1:]
print(dx)

# 📌🐍 -----------------------------------------------------------------------
import pandas as pd


data = {
               'Coursera':['cyber security', 'AL and ML', 'DSA','spark','pyspark','propmt','ui & ux','sql'],
               'fee': [2000,2500,260000,4600,1234,2000,5000,6000],
               'duration': ['30days','40days','35days','90days','15days','7days','9days','10days']
            }

row = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(data , index = row)

print(df.loc['r2'])
print(df.loc[['r2','r4','r6']])
print(df.loc['r1':'r5'])
print(df.loc['r1':'r5':2])
print(df.loc[:,['fee','duration']])
name = input('enter the csv file name :: ')
df.to_csv(f'C:/1-python/Python ADVANCE/Data_sets/{name}.csv')