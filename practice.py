# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:22:09 2023

@author: shrik
"""

## 📌🐍------------------------------------------------------
#Que 1.
lst1 = [1,2,3]
if len(lst1) == 0:
    print('List is Empty!')
else:
    print('list is not Empty.')    

## 📌🐍------------------------------------------------------
#Que2
l1 = [1,2,3,47,9,5]
l2 = [x*x for x in l1]
print(l2)

## 📌🐍------------------------------------------------------
#Que3

dic = {'a':'apple','b':'banana','c':'cat'}
k = input("Enter the key :: ")
if k in dic:
    print('Key Found!')
else :
    print('Key not found, Enter Another Key!')    

## 📌🐍------------------------------------------------------
#Que4

ran1 = range(100,160,10)
dict = {x:x/100 for x in ran1}
print(dict)

## 📌🐍------------------------------------------------------
#Que5

import pandas as pd
data = {
        'Course':['AI','ML','NLP','LLM','Data Science'],
        'Fees':[1000,1000,500,500,1500],
        'Duration':['10 days','10 days','7 days','7 days','20 days']
        }

df = pd.DataFrame(data)

Tutor = ['Shrikant','Sanket','Naik sir','Dhanu sir','Alakh panday']

df.assign(Tutar = Tutor)


## 📌🐍------------------------------------------------------
#Que6

import pandas as pd
data = {
        'Course':['AI','ML','NLP','LLM','Data Science'],
        'Fees':[1000,1000,500,500,1500],
        'Duration':['10 days','10 days','7 days','7 days','20 days']
        }

df = pd.DataFrame(data)

df.to_csv('data.csv')

## 📌🐍------------------------------------------------------
#Que7
import itertools as it
def mult_values(start,step):
    
    counter = it.count(start,step)
    for i in counter:
        print(i)

mult_values(10, 5)

## 📌🐍------------------------------------------------------
#Que8

mul = lambda a,b : a*b
print(mul(7,10))

## 📌🐍------------------------------------------------------
#Que 9 A
import numpy as np
arr = np.array([0,0,0,0,0,6])

if arr.any() == True:
    print('Yes a NON ZERO Number Found')
else :
    print('All are Zero')    

## 📌🐍------------------------------------------------------
#Que 9 B
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,10)
plt.plot(x,'--o',x+2,'-.x',x+5)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()

## 📌🐍------------------------------------------------------
#Que 10

import matplotlib.pyplot as plt
plt.bar(['Java','python','PHP','JavaScript','C#','C++'],[22.2,23.7,8.8,8,7.7,6.7]) 
plt.show()

## 📌🐍------------------------------------------------------



















