# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:40:12 2023

@author: shrik
"""

#operations on dataframe on csv file 'bank_data'

import pandas as pd
import numpy as np
d =pd.read_csv("C:/1-python/Python ADVANCE/Data_sets/crime_data.csv")
df = pd.DataFrame(d)

df.shape                                    #45211,32

df.size                                     #1446752

df.columns

df.columns.values

df.index

df.dtypes

df=df[0:100:3]
df


df.describe()



df2=df[:2]
df2

df=df[:3]
df

df3=df[::-1]
df3

df1=df.rename({1:'one',2:'two'},axis=0)
df1

'''to skip 1 alternate entry'''

df2=df[0:100:2]
df2                     

df2=df2[::-1]
df2



df2=df.convert_dtypes()
print(df2.dtypes)

#accessing first row
df2=df[:1:]
df2

df
df=df.columns
df



df2=df1[:4]
df2

3



df2=df1[:4]
df2



# 📌🐍 -----------------------------------------------------------------------
import pandas as pd
import numpy as np
df=pd.read_csv("C:/1-python/Python ADVANCE/Data_sets/bank_data.csv")
df

df.shape                                    #45211,32

df.size                                     #1446752

df.columns

df.columns.values

df.index

df.dtypes

df=df[0:100:3]
df


df.describe()

df['age']

df[['Murder','Assault']]

df2=df[:2]
df2

df=df[:3]
df

df3=df[::-1]
df3

df['age']=df['age']-10
df


df['age']=df['age']+10
df


df['age']=df['age']*10
df

df=df.rename({'age':'age_count'},axis=1)
df

df1=df.rename({1:'one',2:'two'},axis=0)
df1

'''to skip 1 alternate entry'''

df2=df[0:100:2]
df2                     

df2=df2[::-1]
df2

df.dtypes['age_count']

df2=df.convert_dtypes()
print(df2.dtypes)

#accessing first row
df2=df[:1:]
df2

df
df=df.columns
df

df3=df.iloc[0:3,0:3]
df3


df1=df[['age','default']]
df2=df1[:4]
df2

df2=df.iloc[1,0]
df2


# 📌🐍 ----------------------------------------------------------------------
import pandas as pd
import numpy as np
df=pd.read_csv("C:/1-python/Python ADVANCE/Data_sets/loan.csv")
df

df.shape                                    #45211,32

df.size                                     #1446752

df.columns

df.columns.values

df.index

df.dtypes

df=df[0:100:3]
df


df.describe()

df['id']

df[['id','member_id']]

df2=df[:2]
df2

df=df[:3]
df

df3=df[::-1]
df3

df['age']=df['age']-10
df


df['age']=df['age']+10
df


df['age']=df['age']*10
df

df=df.rename({'id':'user_id'},axis=1)
df

df1=df.rename({1:'one',2:'two'},axis=0)
df1

'''to skip 1 alternate entry'''

df2=df[0:100:2]
df2                     

df2=df2[::-1]
df2

df.dtypes['id']

df2=df.convert_dtypes()
print(df2.dtypes)

#accessing first row
df2=df[:1:]
df2

df
df=df.columns
df


df2=df1[[:4]
df2


df3=df.iloc[0:3,0:3]
df3


df1=df[['age','default']]
df2=df1[:4]
df2

df2=df.iloc[1,0]
df2
# 📌🐍 ------------------------------------------------------------------------