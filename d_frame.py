import pandas as pd 

technology = {
               'Coursera':['cyber security', 'AL and ML', 'DSA'],
               'fee': [2000,2500,260000],
               'durstion': ['3adays','40days','35days']
            }
df = pd.DataFrame(technology)
print(df)
name = input('enter name :: ')
df.to_csv(name)
df.to_excel('data_f.xlsx')


# 📌🐍 -----------------------------------------------------------------------
#basic operation on data frame

import pandas as pd
import numpy as np

data = {
               'Coursera':['cyber security', 'AL and ML', 'DSA','spark','pyspark'],
               'fee': [2000,2500,260000,4600,1234],
               'durstion': ['30days','40days','35days','90days','15days']
            }
row = ['r0','r1','r2','r3','r4']
df = pd.DataFrame(data , index = row)

x = df.shape
print(x)

y = df.size
print(y)

z = df.columns
print(z)

s = df.values
print(s)

m = df.index
print(m)


# output :: 
# (5, 3)
# 15
# Index(['Coursera', 'fee', 'durstion'], dtype='object')
# [['cyber security' 2000 '30days']
#  ['AL and ML' 2500 '40days']
#  ['DSA' 260000 '35days']
#  ['spark' 4600 '90days']
#  ['pyspark' 1234 '15days']]
# Index(['r0', 'r1', 'r2', 'r3', 'r4'], dtype='object')

# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
import numpy as np

data = {
               'Coursera':['cyber security', 'AL and ML', 'DSA','spark','pyspark'],
               'fee': [2000,2500,260000,4600,1234],
               'durstion': ['30days','40days','35days','90days','15days']
            }
row = ['r1','r2','r3','r4','r5']
df = pd.DataFrame(data , index = row)

df2 = df[:3]
print(df2)
#          Coursera     fee durstion
# r1  cyber security    2000   30days
# r2       AL and ML    2500   40days
# r3             DSA  260000   35days

df3 = df.columns[:2]
print(df3)
# Index(['Coursera', 'fee'], dtype='object')


#whenever we want the limited columns and rows use this
df4 = df.iloc[:3,:2]
print(df4)

#          Coursera     fee
# r1  cyber security    2000
# r2       AL and ML    2500
# r3             DSA  260000

# 📌🐍 -----------------------------------------------------------------------
