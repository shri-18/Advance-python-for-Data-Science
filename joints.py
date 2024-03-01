# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:30:04 2023

@author: shrik
"""

# 📌🐍 -----------------------------------------------------------------------
#

import pandas as pd
import numpy as np

tech1 = {'courses':['cyber Security', 'Data Science',
                   'React','python',],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month',
                    '4 months'],
        
        }

tech2 = {'courses':['nodeJS', 'django',
                   'Data Science',
                   'python'],
        'Discount':[20,45,34,65]
        }
lab = ['r1','r2','r3','r4',]
lables = ['r2','r6','r3','r5']

df1 = pd.DataFrame(tech1 , index=lab)
df2 = pd.DataFrame(tech2 , index=lables)

print(df1)
print('\n')
print('                   **************************                         ')
print('\n')
print(df2)
# 📌🐍 -----------------------------------------------------------------------
#left join
df3 = df1.join(df2, lsuffix='_left', rsuffix='_right')
df3

#output
'''
 courses_left  prices  Duration courses_right  Discount
r1   cyber Security    2000  2 months           NaN       NaN
r2     Data Science    3000  3 months        nodeJS      20.0
r3            React    4000   1 month           NaN       NaN
r4  Web Development    6000  4 months           NaN       NaN
'''
# 📌🐍 -----------------------------------------------------------------------
#inner join
#it gives the element having same lables
df4 = df1.join(df2, lsuffix="_left", rsuffix="_right", how = 'inner' )
print(df4)

#output
''' courses_left  prices  Duration courses_right  Discount
r2  Data Science    3000  3 months        nodeJS        20'''


# 📌🐍 -----------------------------------------------------------------------
#right join
df5 = df1.join(df2, lsuffix="_left", rsuffix="_right", how = 'right')
print(df5)

#output
'''
 courses_left  prices  Duration courses_right  Discount
r2  Data Science  3000.0  3 months        nodeJS        20
r6           NaN     NaN       NaN        django        45
r3         React  4000.0   1 month  Data Science        34
r5           NaN     NaN       NaN        python        65
'''
# 📌🐍 -----------------------------------------------------------------------
#inner , left, right join using coloumns as index

df6 = df1.set_index('courses').join(df2.set_index('courses'), how = 'inner')
print(df6)

#output
#              prices  Duration  Discount
#courses                                 
#Data Science    3000  3 months        34
#python          6000  4 months        65

#right
df7 = df1.set_index('courses').join(df2.set_index('courses'), how = 'right')
print(df7)

#output
'''
              prices  Duration  Discount
courses                                 
nodeJS           NaN       NaN        20
django           NaN       NaN        45
Data Science  3000.0  3 months        34
python        6000.0  4 months        65
'''

#left
df8 = df1.set_index('courses').join(df2.set_index('courses'), how = 'left')
print(df8)

#output
'''
                prices  Duration  Discount
courses                                   
cyber Security    2000  2 months       NaN
Data Science      3000  3 months      34.0
React             4000   1 month       NaN
python            6000  4 months      65.0
'''
# 📌🐍 -----------------------------------------------------------------------
#using pandas.mearge() method for inner join

d1 = pd.merge(df1,df2)
print(d1)

#output
'''
        courses  prices  Duration  Discount
0  Data Science    3000  3 months        34
1        python    6000  4 months        65
'''
# 📌🐍 -----------------------------------------------------------------------
#concat operation  (extend comman coloums in both dataframes and simply 
#join the two data frames)
data = [df1, df2]
d2 = pd.concat(data)
print(d2)

#output
'''           courses  prices  Duration  Discount
r1  cyber Security  2000.0  2 months       NaN
r2    Data Science  3000.0  3 months       NaN
r3           React  4000.0   1 month       NaN
r4          python  6000.0  4 months       NaN
r2          nodeJS     NaN       NaN      20.0
r6          django     NaN       NaN      45.0
r3    Data Science     NaN       NaN      34.0
r5          python     NaN       NaN      65.0'''

# 📌🐍 -----------------------------------------------------------------------




























