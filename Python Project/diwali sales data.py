# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:20:11 2024

@author: wario
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importing the csv data file
import csv

csv_file_path = r'C:\Users\wario\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row)
        
cvs_file_path =  r'C:\Users\wario\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv'
df = pd.read_csv(csv_file_path, encoding= 'unicode_escape')

print(df.head()) 

df.shape       
df.info()        

#data cleaning
#drop blank columns
df.drop(['Status','unnamed1'], axis=1, inplace=True)

#check all null values
pd.isnull(df).sum()

#drop null values
df.dropna(inplace=True)

df.shape

#changing data types
df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtypes

df.columns

df.describe()

#use describe functions for specific columns
df[['Age','Orders','Amount']].describe()



# plotting abar chart for gender and its count.

ax =  sns.countplot(x = 'Gender', data =df)

for bars in ax.containers:
    ax.bar_label(bars)
    
# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending= False)

sns.barplot(x='Gender', y= 'Amount', data = sales_gen)


# plotting chart for gender by age group
ax = sns.countplot(data=df, x= 'Age Group', hue= 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)
    
#plotting chart  for total amount/sales from top 10 states
sales_state= df.groupby(['State'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending= False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_state, x='State', y='Amount')


#plotting top 10  most sold products
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending= False).plot(kind= 'bar')