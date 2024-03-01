# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:08:02 2023

@author: shrik
"""
_______________________________________________________________________________
#'''query'''
import pandas as pd
data = {
               'Courses':['cyber security', 'AL and ML', 'DSA','spark','pyspark'],
               'fee': [2000,2500,260000,4600,1234],
               'duration': ['30days','40days','35days','90days','15days'],
               'Discount' : [10,10,10,15,20],
            }

row = ['r1','r2','r3','r4','r5']
df = pd.DataFrame(data , index = row)
df2 = df.query("Courses == 'spark'")
print(df2)

#'''add new coloumn''' 
tutors = ['shrikant','amar','prathamesh','sanket','yash']
df3 = df.assign(TutorsAssigned = tutors)
print(df3)


#'''add multiple columns'''
mnc = ['TATA','HCL','Infosys','Google','Amazon']
df4 = df.assign(MNC = mnc , tutors = tutors)
print(df4)

#derive one coloumn fron existing coloumn
#using lambda function
df5 = df.assign(Discount_persent= lambda x: x.fee * x.Discount/100)
print(df5)

#for adding coloumn in original dataframe
df["MNS's"] = mnc
print(df)

#add mew coloumn at specific location
df.insert(0,'Tutors', tutors)
df

#for counting the size of dataframe
#number of coloumns and rows

row_count = len(df.index)
row_count

col_count = len(df.axes[1])
col_count

df.size

df.shape

df.shape[0]                #for row count
df.shape[1]                #for coloumn count







  