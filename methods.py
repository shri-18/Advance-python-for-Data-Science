# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:44:18 2023

@author: shrik
"""

#to select the row where score is missing using isnull() method
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

print(df[df['score'].isnull()])
_____________________________________________________________________________
#programm to select rows scores between 15 and 20
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)
print(df[df['score'].between(15,20)])
_____________________________________________________________________________
#programm to select rows scores between greater than 15 and attempts less than 2

#.between(range)method
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)
print(df[(df['score'].between(15,20)) & (df['attempts'] < 2)])
_____________________________________________________________________________

#programm to change the score in d row to 11.5
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

df.loc['d','score'] = 11.5
print(df)
_____________________________________________________________________________
#programm to find the examination attempt by the student
#.sum()method
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)
print(df['attempts'].sum())

_____________________________________________________________________________
#programm to  calculate the mean of all student score
#.mean()method
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

print("MEAN :: ",df['score'].mean())
_____________________________________________________________________________
#programm to append new row 
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

df.loc['k'] = ['Vishvajeet', 18.5,2,'yes']
print(df)


_____________________________________________________________________________
#programm to sort data frame 1st name in descending order then by score in ascending order

import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

#by name descending order

#df1 = df.sort_values(by = ['name','score'],ascending=[False,True])
df1 = df.sort_values(by = ['name'],ascending=[False])

#score by ascending order
df2 = df.sort_values(by = ['score'], ascending=[True])
print(df1)
print('\n')

print(df2)

_____________________________________________________________________________
#programm to replace qualify column cotains values yes and no with true and false
#map method
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

df['qualify'] = df['qualify'].map({'yes':True,'no':False})
df
_____________________________________________________________________________
#programm to replace chetan with dinesh

#.replace() method
import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

df['name'] = df['name'].replace({'chetan':'dinesh'})
df

_____________________________________________________________________________
#programm to insert new coloumn to data set

import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

color = ['red','blue','white','black','grey','yello','violet','orange','green','marroon']
df['color'] = color
df
df.loc['l'] = ['shri',10,2,'no','purple']
df
_____________________________________________________________________________
#programm to iterate data frame

import pandas as pd
import numpy as np
exam_data = {
    'name':['shrikant','amar','prathamesh','sanket','yash','pranav','chetan','mahesh','pratik','dhanu'],
    'score':[19,9,np.nan,9,20,15,np.nan,9,18,9],
'attempts': [1,3,2,1,2,1,1,1,4,2]     ,
'qualify':['yes','no','yes','yes','no','yes','no','no','yes','yes']
    }

lables = ['a','b','c','d','e','f','g','h','i','j']
df =pd.DataFrame(exam_data,index = lables)

for index, row in df.iterrows():
    print(row['name'],row['score'])

_____________________________________________________________________________
#programm to 

l = lambda x : x+2
print(l(2))