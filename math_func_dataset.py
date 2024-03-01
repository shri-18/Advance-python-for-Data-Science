# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:19:25 2023

@author: shrik
"""
# 📌🐍 -----------------------------------------------------------------------
#math function on dataset

import pandas as pd
import numpy as np

data = { 'A':[1,2,3],
      'B':[9,8,7],
      'C':[4,5,6]
      }

df = pd.DataFrame(data)
print(df)

def add_3(x):
    return x + 3

#apply() method
df2 = df.apply(add_3)
print(df2)

# 📌🐍 -----------------------------------------------------------------------
#apply method for spacific coloumns
def add_4(x):
    return x + 4
    
df['B'] = df['B'].apply(add_4)
print(df)

df[['A','C']] = df[['A','C']].apply(add_4)
print(df)

# 📌🐍 -----------------------------------------------------------------------
#apply method using lambda function

df2 = df.apply(lambda x: x+3)
print(df2)

#for Coloumns
df[['A','C']] = df[['A','C']].apply(lambda x : x+3)
print(df)

# 📌🐍 -----------------------------------------------------------------------
#Transform function
#used instead apply funtion

def mul_2(x):
    return x * 2

df = df.transform(mul_2)
print(df)

#for multiple coloumns
#and creatinf another dataframe to store this information
def mul_0(x):
    return x * 0

df3 = df[['A','B']].transform(mul_0)
print(df3)

# 📌🐍 -----------------------------------------------------------------------
#map method
df['A'] = df['A'].map(lambda A : A/2)
print(df)

# 📌🐍 -----------------------------------------------------------------------
#Groupby () method

import pandas as pd
import numpy as np

data = {'courses':['cyber Security', 'Data Science',
                   'AI and ML','Web Development',
                   'python','Data Science', 'AI and ML'],
        'prices':[2000,3000,4000,6000,300,9000,7000],
        'Duration':['2 months','3 months','1 month','4 months','2 months','2 months','1 month'],
        'Discount':[20,45,34,65,12,56,340]
        }

df = pd.DataFrame(data)
print(df)

df1 = df.groupby(['courses']).sum()
df1

#for multiple coloumns
df2 = df.groupby(['courses']).sum()
df2
df2 = df.groupby(['Duration']).sum()
df2

df3 = df.groupby(['courses','Duration']).sum().reset_index()
df3
# 📌🐍 -----------------------------------------------------------------------


import pandas as pd
import numpy as np

data = {'courses':['cyber Security', 'Data Science',
                   'AI and ML','Web Development',
                   'python','Data Science', 'AI and ML'],
        'prices':[2000,3000,4000,6000,300,9000,7000],
        'Duration':['2 months','3 months','1 month','4 months','2 months','2 months','1 month'],
        'Discount':[20,45,34,65,12,56,340]
        }

df = pd.DataFrame(data)
df1 = df.columns
print(df1)

# 📌🐍 -----------------------------------------------------------------------



