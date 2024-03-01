# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:31:24 2023

@author: shrik
"""
# 📌🐍 -----------------------------------------------------------------------

'''Numpy library is popular open source library used for scientific 
calculation or scientific computing applications, and it stands for 
Numerical python,it consist multidimentional array objects and 
collection of routines for processing'''

# 📌🐍 -----------------------------------------------------------------------

#create ndarray

import numpy as np

arr = np.array([10,20,30])
print(arr)
type(arr)

#creation of multy diamentional array

arr1 = np.array([[10,20,30],
                 [40,50,60]])
print(arr1)
type(arr1)


arr3 = np.array([10,20,30,40], ndmin = 3)
print(arr3)

arr4 = np.array([10,20,30],dtype = complex)
print(arr4)

#Properties of numpyarray
import numpy as np
n = 3
arr5 = np.array([[1,2,3],
                 [4,0,6],
                 [7,8,9]])

for x in arr5:
    for i in range(n):
        if x[i] == 0:
            x[:,i] = 0
            print(x)

print(arr5.ndim)
print(arr5)

arr6 = np.array([10,20,30])
print("each items contain in bytes : ",arr6.itemsize)
print("Each item is of type :: ", arr6.dtype)
print('Array size :: ', arr6.size)
print('Shape :: ',arr6.shape)
import numpy as np
#indexing in numpy array
arr = np.arange(0,20,3)
print("A sequntial array with stapsof 3:\n ",arr)
import numpy as np
arr = np.arange(11)
print(arr)

print(arr[2])
print(arr[-1])

import numpy as np

arr = np.array([[10,20,30,40],[50,60,70,80]])

print(arr)

print(arr.shape)

print(arr[1,1])

#access Array element using slicing
arr = np.array([0,1,2,3,4,5,6,7,8,9])
x = arr[1:8:2]
print(x)

print(arr[1:8:-2])
print(arr[-2:3:-1])
print(arr[-2:10])

import numpy as np

#indexing in numpy
multi_arr = np.array([[10,20,10,40],
                [40,50,70,90],
                [50,70,60,80],
                [30,90,40,70]])
# multi_arr

# multi_arr[1,2]             #arr[row, col]
# multi_arr[1:]

print(multi_arr[:3, ::2])

import numpy as np
arr = np.arange(35).reshape(5, 7)
print(arr)

'''[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]'''

arr = np.arange(1,37).reshape(6,6)
print(arr)

'''
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]
 [13 14 15 16 17 18]
 [19 20 21 22 23 24]
 [25 26 27 28 29 30]
 [31 32 33 34 35 36]]
'''

arr = np.arange(12).reshape(3, 4)
print(arr)

'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''

rows = np.array([False,True,True])
#where there is true rows only that rows will be shown
wanted_rows = arr[rows,:]      
print(wanted_rows)
'''[[ 4  5  6  7]
 [ 8  9 10 11]]'''

#convert NDArray to list

lst = arr.tolist()
print(type(lst))
print(lst)


l = [1,2,3,4]
arr = np.array(l)
print(arr)






def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    # Find the rows and columns that contain zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set entire rows and columns to zero
    for row in zero_rows:
        matrix[row] = [0] * cols

    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0

    return matrix

# Test examples
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
result1 = setZeroes(matrix1)
print(result1)

matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
result2 = setZeroes(matrix2)
print(result2)
