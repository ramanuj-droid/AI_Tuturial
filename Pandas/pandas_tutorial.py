"""
Pandas represents tabular data and how to load and inspect datasets.
In ML pipelines, Pandas is the entry point for most datasets (CSV, Excel, databases).
"""
import pandas as pd

#Series : A 1-dimensional labeled array.
s = pd.Series([10,20,30,40,50])

#DataFrame : A 2-dimensional table (rows + columns).

import pandas as pd

data = {
    "Name": ["Ram","Shyam","Kewat","Riya","Aman"],
    "Age": [23,45,34,21,30],
    "Salary": [40000,70000,50000,35000,60000]
}

df = pd.DataFrame(data)

#LOADING DATA

""" 
df = pd.read_csv("data.csv")
CSV
Excel
JSON
SQL databases

data = pd.read_csv("data.csv")
data.head()
"""
"""
1)df.head() -> 5 upper
2)df.tail() -> 5 lower
3)df.info() -> full
4)df.describe() -> stats
5)df.columns -> column name
"""

#Inserting New Column

df["Bonus"] = df["Salary"] * 0.10

 #Data Selection & Filtering

 #.loc selects data using column names and index labels.

#print(df.loc[2],df.loc[:, "Name"],df.loc[:, ["Name","Salary"]],df.loc[1:3, ["Name","Age"]])

#.iloc[] — Position Based Selection : .iloc uses numerical positions, not labels.

#print(df.iloc[2],df.iloc[0:3, 0:2])

#Boolean Filtering

df[df["Age"] > 30]
df[(df["Age"] > 25) & (df["Salary"] > 50000)]

#Sorting 
df.sort_values("Age")
#Unique
df["Age"].unique() 

#Data Cleaning
"""
#to check empty data
print(df.isnull().sum())

#Remove Rows with Missing Values
df.dropna()

#Fill Values
df["Salary"].fillna(df["Salary"].median(), inplace=True)

#remove duplicates
df.drop_duplicates()

#rename 
df.rename(columns={"Salary":"Income"}, inplace=True)
"""
#FEATURE ENGINEERING : CREATING DATA FROM EXISTING DATA

df['Total_income_tax'] = df['Salary'] *5/100

#Apply F(x)

def salary_category(x):
    if x > 60000:
        return "High"
    elif x > 40000:
        return "Medium"
    else:
        return "Low"

df["Salary_Category"] = df["Salary"].apply(salary_category)

#map() Function : Used to replace values using a dictionary.

gender = {
    "Ram":"Male",
    "Shyam":"Male",
    "Kewat":"Male",
    "Riya":"Female"
}

df["Gender"] = df["Name"].map(gender)

"""
Binning (Grouping Numeric Values)
Convert continuous values into categories.
Example: Age → Young / Middle / Senior
Using cut():
"""

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,25,40,60],
    labels=["Young","Middle","Senior"]
)

#GroupBy & Aggregation (Core of EDA)
"""
Goal: summarize patterns in data.

GroupBy allows you to answer questions like:

- average salary by department
- total sales by region
- number of customers by city
"""

#GROUP BY
df.groupby("Age")

#COUNT
df.groupby("Department")["Name"].count()

#Table Merging

"""

merge() --> SQL JOIN - LET,FULL ,RIGHT INNER ,OUTER

import pandas as pd

employees = pd.DataFrame({
    "EmpID":[1,2,3],
    "Name":["Ram","Shyam","Riya"]
})

salary = pd.DataFrame({
    "EmpID":[1,2,3],
    "Salary":[40000,50000,60000]
})

merged = pd.merge(employees, salary, on="EmpID")
print(merged)

concat() : concat() — Combine Rows or Columns
         : concat() stacks data.

Example datasets.

df1 = pd.DataFrame({
    "Name":["Ram","Shyam"],
    "Age":[23,45]
})

df2 = pd.DataFrame({
    "Name":["Riya","Aman"],
    "Age":[21,30]
})

pd.concat([df1, df2])

join()

join() — Index-Based Merge 
       — join() merges using index values.

Example: df1.join(df2)

"""
