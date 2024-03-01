# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:06:11 2023

@author: shrik
"""
# 📌🐍 -----------------------------------------------------------------------
#to get the version of numpy or any library
import numpy as np
print(np.__version__)

# 📌🐍 -----------------------------------------------------------------------
#write program to taste whether the none of the element is zero
import numpy as np

x = np.array([1,2,3,4])
print('Original Array :: ',x)
print("Taste :: ",np.all(x))

y = np.array([0,1,2,3])
print("Taste :: ",np.all(y))

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to taste any of the element of th given array is nonzero

x = np.array([0,0,0,0,5])
print("Taste:: ",np.any(x))

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to taste a given array element for
# finite ness (not infinity nor a number)

import numpy as np

a = np.array([1,0,np.nan,np.inf])

print("Originla Array :: ",a)

print('finiteness :: ',np.isfinite(a))

#Originla Array ::  [ 1.  0. nan inf]
#finiteness ::  [ True  True False False]

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to taste element wise nan value of agven array

import numpy as np

a = np.array([1,0,np.nan,np.inf])

print("Originla Array :: ",a)

print("Taste :: ",np.isnan(a))

#Originla Array ::  [ 1.  0. nan inf]
#Taste ::  [False False  True False]

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to do the create an element wise comparison 

#np.greter()
#np.greater_equal()
#np.less()
#np.less_equal()
import numpy as np
x = np.array([3,5])
y = np.array([2,5])

print("Original :: ",x ," and ",y)

print("Greater :: ",np.greater(x,y))
print("Greater_Equal :: ",np.greater_equal(x,y))
print("Greater :: ",np.less(x,y))
print("Greater :: ",np.less_equal(x,y))
# 📌🐍 -----------------------------------------------------------------------
#numpy programm to create the 3*3 identity matrics

import numpy as np
arr = np.identity(3)
print(arr)

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to generate random number (using normal distribution)
import numpy as np
rand_no = np.random.normal(0,1,2)                   #(start,end,quantity)
print("Random number Between 0 & 1 :: ", rand_no)

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to uniform distribution

import numpy as np
rand_no = np.random.uniform(0,1,2)                   #(start,end,quantity)
print("Random number Between 0 & 1 :: ", rand_no)

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to create 3*4 array and iterate over it
import numpy as np
a = np.arange(10,22 ).reshape(3,4) 
print ('Original :: ',a)

print('Iterated ::' ,end= ' ')

for x in np.nditer(a):
    print(x,end=' ')
    
# 📌🐍 -----------------------------------------------------------------------
#numpy programm to create a vector of length  5 with all the element evenly distributed from 10 to 50

import numpy as np
v = np.linspace(10, 49, 5)
print(v)

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to create 3*3 mytrics with value ranging from 2 to 20

import numpy as np
a = np.arange(2,11 ).reshape(3, 3)
print(a)

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to create array the first element become last
import numpy as np

a = np.arange(12,38)
print('Original :: ', a)
print('Reversed :: ', a[::-1])

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to create the vectors

import numpy as np
x = np.array([[1,2],[2,3]])
y = np.array([[3,4],[5,6]])

dt = np.dot(x,y)

print('Dot product :: ',dt)


cx = np.cross(x, y)
print('Cross product :: ',cx)


# 📌🐍 -----------------------------------------------------------------------
#numpy programm to compute aigen values and eigen vectors from the given array

import numpy as np

m= np.mat("3 -2;1 0")
print("a\n",m)

w,v = np.linalg.eig(m)
print("Eigen values of matrix w :: ",w) 
print("Eigen values of matrix v :: ",v)

# 📌🐍 -----------------------------------------------------------------------
#numpy programm to compute the inverse of the given matrix
import numpy as np
m = np.array([[1,2],[3,4]])
#for inverse
res = np.linalg.inv(m)

print('Inverse :' ,res)

import itertools

print(.combination(2))

