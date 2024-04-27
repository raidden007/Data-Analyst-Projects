import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

df=pd.read_csv('D:\DATA ANALYTICS\DA projects\IBM HR Analytics -Attrition and performance\HR-Employee-Attrition.csv')
df.head()

df.dtypes                               # Know the data types of each column

df.isnull().any()                       # Scrubbing the data


# Bring Attrition column to first.
front=df['Attrition']                   
df.drop(labels=['Attrition'],axis=1,inplace=True)
df.insert(0,'Attrition',front)
df.head()

# Dropping unwanted records
df.drop(labels=['EmployeeCount','EmployeeNumber','StockOptionLevel','StandardHours'],axis=1,inplace=True)
df.head()

df['Gender']= df['Gender'].map({'Male': 0, 'Female': 1})

Attrition = {'Yes':1, 'No':0}
df.Attrition = [Attrition[item] for item in df.Attrition]

# Get categorical/unique values of coulmn
df.EducationField.unique() 

# creating a dict file 
Gender={'Male':1,'Female':0}
# traversing through dataframe Gender column and writing values where key matches
df.Gender=[Gender[item] for item in df.Gender]

Field={'Life Sciences':2,'Medical':1,'Other':0,'Marketing':3,'Technical Degree':4,'Human Resources':5}
df.EducationField=[Field[item] for item in df.EducationField]

-----------------------------------------------------------------



# Attrition Rate ####

Attrition_Rate=df.Attrition.value_counts()/len(df)
Attrition_Rate                             # 83% of employees Stayed. 
                                           # 16% of employees left.


## Employee Income & Gender Vs Attrition.

sns.barplot(x='Attrition',y='MonthlyIncome',hue='Gender',data=df,color='green').set_title('Employee Income Gender Distribution')
plt.figure(figsize=(10, 10))
plt.show()

## Employee salary vs Attrition #####

df['Income_Range']=pd.cut(df['MonthlyIncome'],[1000,5000,10000,15000,20000])

f, ax = plt.subplots(figsize=(15, 4))
sns.countplot(y='Income_Range',hue='Attrition',data=df).set_title('Employee Salary Attrition Distribution')
plt.plot()


# Employee Job satisfaction rating vs Attrition ####

fig=plt.figure(figsize=(15,4))
ax=sns.kdeplot(df.loc[(df['Attrition']==0),'JobSatisfaction'],color='g',shade=False,label='No Attrition')
ax=sns.kdeplot(df.loc[(df['Attrition']==1),'JobSatisfaction'],color='r',shade=True,label='Attrition')
ax.set(xlabel='Employee Job Satisfaction Rating',ylabel='Frequency')
plt.title('Employee Job Satisfaction Rating - Attrition vs No Attrition')


# Employee Work-life Balance rating vs Attrition

fig=plt.figure(figsize=(15,4))
ax=sns.kdeplot(df.loc[(df['Attrition']==0),'WorkLifeBalance'],color='g',shade=False,label='No Attrition')
ax=sns.kdeplot(df.loc[(df['Attrition']==1),'WorkLifeBalance'],color='r',shade=True,label='Attrition')
ax.set(xlabel='Employee WorkLifeBalance Rating',ylabel='Frequency')
plt.title('Employee WorkLifeBalance Rating - Attrition vs No Attrition')


# Employee YearsAtCompany vs Attrition

fig=plt.figure(figsize=(15,4))
ax=sns.kdeplot(df.loc[(df['Attrition']==0),'YearsAtCompany'],color='g',shade=False,label='No Attrition')
ax=sns.kdeplot(df.loc[(df['Attrition']==1),'YearsAtCompany'],color='r',shade=True,label='Attrition')
ax.set(xlabel='Employee YearsAtCompany ',ylabel='Frequency')
plt.title('Employee YearsAtCompany - Attrition vs No Attrition')


fig=plt.figure(figsize=(15,8))
value=df['YearsAtCompany']<11
df3=df[value]
sns.countplot(x='YearsAtCompany',hue='Attrition',data=df3)
plt.show()                                                      ## Employee leaving the company at initial stage.


# Employee YearsSinceLastPromotion vs Attrition

fig=plt.figure(figsize=(10,6))
sns.countplot(x='YearsSinceLastPromotion',hue='Attrition',data=df,color='green')
plt.show()    

-----------------------------------------------------------------------------------------------------------------
# Analysis of different parameter Vs Attrition ##########

total_records= len(df)
columns = ["Gender","MaritalStatus","WorkLifeBalance","EnvironmentSatisfaction","JobSatisfaction",
           "JobLevel",'NumCompaniesWorked',"JobInvolvement","BusinessTravel",'Department']

j=0
for i in columns:
    j +=1
    plt.subplot(5,2,j)
    ax1 = sns.countplot(data=df,x= i,hue="Attrition")
    if(j==9 or j== 10):
        plt.xticks( rotation=90)
    for p in ax1.patches:
        height = p.get_height()
         

# Custom the subplot layout
plt.subplots_adjust(bottom=0.1, top=4)
plt.show()

--------------------------------------------------------------------------------------------------------------------




                                                     













    
    
    
