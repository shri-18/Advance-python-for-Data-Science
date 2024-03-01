# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:31:02 2023

@author: shrik
"""

import pandas as pd

d = pd.read_csv("C:/1-python/Python ADVANCE/Data_sets/Seeds_data.csv")
df = pd.DataFrame(d)

#using shape property
print('No of rows :: ', df.shape[0])
print('No of Coloumns :: ', df.shape[1])

print("---------------------Another Method---------------------------")

#using axes
print('No of rows :: ', len(df.axes[0]))
print('No of Coloumns :: ',len(df.axes[1]))

#info method of dataframes
print(df.info())

#display specific Coloumns
print(df[['length','Width']])

#display specific rows and coloumns
print(df.loc[[4,67,100,200],['Area','Compactness']])

#area values greater than 15
print(df[df['Area'] > 15])

#Query 
print(df.query("Area == 15.38"))

#deriving coloumn from area and length coloumn
df1 = df.assign(Volume = lambda x : x.Area * x.length)
print(df1)

#isnull()
print(df[df['Compactness'].isnull()])

#between()
print(df[df['Area'].between(10,13)])

#sum()
print(df[df['Compactness'].sum()])

#mean()
print(df[df['Type'].mean()])

#sort_values
df2 = df.sort_values(by = ['Area'], ascending=[True])
print(df2)

#iterating dataframe
for index, row in df.iterrows():
    print(row['Area'])

#Shuffle rows

       
    