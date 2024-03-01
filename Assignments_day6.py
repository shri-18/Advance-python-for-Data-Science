# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:01:04 2023

@author: shrik
"""

#wriet pandas programm to create f=dataframe from dictionary and display it

import pandas as pd

d = {
     'X':[1,2,3,4,5],
     'Y':[12,23,34,45,56],
     'Z':[123,234,345,456,567]
     }

df = pd.DataFrame(d)
print(df)

_____________________________________________________________________________
#write a program to create a data frame 
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[12.3,9,np.nan,9,20,14.5,np.nan,9,8,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

labels = ['a','b','c','d','e','f','g','h','i','j']
len(labels)

df =pd.DataFrame(exam_data,index = labels)
print(df)
df.info()
_____________________________________________________________________________

#print(1st 3 rows) of dataframe
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[12.3,9,np.nan,9,20,14.5,np.nan,9,8,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']


df =pd.DataFrame(exam_data,index = lables)
print(df.iloc[0:3])

_____________________________________________________________________________
#write python program to select name and score coloumn 
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[12.3,9,np.nan,9,20,14.5,np.nan,9,8,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

df1 = df[['name','score']]
df1
_____________________________________________________________________________
#write program to select specific coloumn and rows

import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[12.3,9,np.nan,9,20,14.5,np.nan,9,8,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

df1 = df.loc[['b','d','f','j'] , ['score','qualify']]
df1
_____________________________________________________________________________
# print the rows having attempts more thn 2
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[12.3,9,np.nan,9,20,14.5,np.nan,9,8,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)
print('Number of attempt greter than 2')
print(df[df['attempts'] > 2])
_____________________________________________________________________________
#no of rows and cols
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[12.3,9,np.nan,9,20,14.5,np.nan,9,8,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)


print('No of rows :: ', df.shape[0])
print('No of Coloumns :: ', df.shape[1])
#No of rows ::  10
#No of Coloumns ::  4
print("---------------------Another Method---------------------------")

print('No of rows :: ', len(df.axes[0]))
print('No of Coloumns :: ',len(df.axes[1]))
_____________________________________________________________________________
