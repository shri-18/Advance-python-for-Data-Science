# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:16:28 2023

@author: shrik
"""
# 📌🐍 -----------------------------------------------------------------------
#shuffle dataframe rows

import pandas as pd
import numpy as np

data = {'courses':['cyber Security', 'Data Science',
                   'AI and ML','Web Development',
                   'python','Data Science', 'AI and ML'],
        'prices':[2000,3000,4000,6000,300,9000,7000],
        'Duration':['2 months','3 months','1 month',
                    '4 months','2 months','2 months','1 month'],
        'Discount':[20,45,34,65,12,56,340]
        }

df = pd.DataFrame(data)

#foe shuffle use sample method the quantity of element 
#of controlled by frac out of 1
df1 = df.sample(frac=1)
print(df1)

#courses  prices  Duration  Discount
#0   cyber Security    2000  2 months        20
#4           python     300  2 months        12
#2        AI and ML    4000   1 month        34
#5     Data Science    9000  2 months        56
#6        AI and ML    7000   1 month       340
#1     Data Science    3000  3 months        45
#3  Web Development    6000  4 months        65

df2 = df.sample(frac=0.25)
print(df2)

#courses  prices  Duration  Discount
#4     python     300  2 months        12
#2  AI and ML    4000   1 month        34

df3 = df.sample(frac=0.5)
print(df3)

 #courses  prices  Duration  Discount
#4           python     300  2 months        12
#3  Web Development    6000  4 months        65
#5     Data Science    9000  2 months        56
#2        AI and ML    4000   1 month        34


#reset index

df4 = df.sample(frac=1).reset_index(drop = True)
print(df4)

#courses  prices  Duration  Discount
#0        AI and ML    7000   1 month       340
#1  Web Development    6000  4 months        65
#2     Data Science    3000  3 months        45
#3        AI and ML    4000   1 month        34
#4     Data Science    9000  2 months        56
#   cyber Security    2000  2 months        20
#6           python     300  2 months        12


#in reset_index(drop = True) means the old index is to should be deleted 
#and new index created for the newly shuffle element


# 📌🐍 -----------------------------------------------------------------------

