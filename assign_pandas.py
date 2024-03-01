import pandas as pd
ds = pd.Series([2,3,4,5])

# 📌🐍 -----------------------------------------------------------------------
print('Pandas series and type')
print(ds)
print('Convert to list')
print(ds.tolist())
# 📌🐍 -----------------------------------------------------------------------

# panda programm to add, substract ,multiply

# sample series = [2,4,6,8,10],[1,3,5,7,9]

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])

add = ds1 + ds2
print(add)

sub = ds1 - ds2
print(sub)

mul = ds1*ds2
print(mul)

div = ds1 / ds2
print(div)
# 📌🐍 -----------------------------------------------------------------------
# create a pandas series and compare both series
import pandas as pd

ds = pd.Series([2,4,6,8,10])
ds1 = pd.Series([1,3,5,7,9])
 
print('Series 1')
print(ds)
print('Series 2')
print(ds1)
print('Equal')
print(ds == ds1)
print('Greater than : ')
print(ds > ds1)
# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
d1 = {'a':100,'b':200,'c':300,'d':400,'e':800}
print('Original Dictionary')
print(d1)
ds = pd.Series(d1)

print(ds)
# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
import numpy as np
n_a = np.array([1,2,3,4])
ds = pd.Series(n_a)
print('Numpy Array :: ',n_a) 
print("Series :: ")
print(ds)

x = pd.to_numeric(ds, errors='coerce')
print(x)
# 📌🐍 -----------------------------------------------------------------------

import pandas as pd

d = {
    'a':[1,2,3,4,5,6],
    'b':[5,6,7,8,9,12],
    'c':[3,2,1,12,23,34]
}
df = pd.DataFrame(data=d)
print('Original Data frame')
print(df)
d1 = df.iloc[:,0]
print(d1)
# 📌🐍 -----------------------------------------------------------------------
import pandas as pd
s = pd.Series([
    ['red','green','white'],
    ['red','black','hue'],
    ['yellow']
])

print('Original Sries : ')
print(s)

# stack function is used to stack the prescribed level(s) from columns of index
s = s.apply(pd.Series).stack().reset_index(drop=True)

print('New :')
print(s)
# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
s = pd.Series([
    ['red','green','white'],
    ['red','black','hue'],
    ['yellow']
])

print('Original Sries : ')
print(s)

s1 = s.apply(pd.Series)
s2 = s1.stack()
s2
s1
s3 = s2.reset_index(drop=True)
print(s3)

# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
ds = pd.Series(['100','python','300.5','300','400'])
print('Original Series :: ')
print(ds)
s = pd.Series(ds).sort_values()
print(s)
new_s = pd.concat([ds,pd.Series(['500','php'])])
print(new_s)

# 📌🐍 -----------------------------------------------------------------------
# reindex method in pandas
import pandas as pd
ds = pd.Series(data= [1,2,3,4,5], index= ['a','b','c','d','e'])
print('originaL :: ')
print(ds)
ds =ds.reindex(index=['b','a','c','d','e'])
print('new :: ')
print(ds)

# output
# originaL :: 
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64
# new ::
# b    2
# a    1
# c    3
# d    4
# e    5
# dtype: int64
# 📌🐍 -----------------------------------------------------------------------

