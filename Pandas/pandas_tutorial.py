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