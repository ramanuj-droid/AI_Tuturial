"""
EDA Mini Project — Workflow
Steps:
Load dataset
Inspect dataset
Handle missing values
Explore distributions
Detect outliers
Analyze feature relationships
Correlation analysis
Final insights
"""

# Housing Dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# STEP 1 — LOAD DATASET
# Read the dataset from a CSV file

df = pd.read_csv("housing.csv")

# Display the first 5 rows of the dataset
print(df.head())

# STEP 2 — INSPECT DATASET STRUCTURE
print(df.info())
print(df.describe())

# STEP 3 — CHECK MISSING VALUES
print(df.isnull().sum())

df["GarageArea"].fillna(df["GarageArea"].median(), inplace=True)
df["BedroomAbvGr"].fillna(df["BedroomAbvGr"].median(), inplace=True)

# STEP 4 — VISUALIZE TARGET VARIABLE DISTRIBUTION
# Create a figure with specific size

plt.figure(figsize=(8,5))

sns.histplot(df["SalePrice"], kde=True)
plt.title("Distribution of House Prices")
plt.show()

# STEP 5 — OUTLIER DETECTION : Create figure

plt.figure(figsize=(8,5))
sns.boxplot(x=df["SalePrice"])
plt.title("House Price Outliers")
plt.show()
# STEP 6 — RELATIONSHIP BETWEEN FEATURES

plt.figure(figsize=(8,5))
sns.scatterplot(x="GrLivArea", y="SalePrice", data=df)
plt.title("Living Area vs House Price")
plt.show()

# STEP 7 — CORRELATION ANALYSIS

corr = df.corr(numeric_only=True)

plt.figure(figsize=(12,8))
sns.heatmap(corr, cmap="coolwarm", annot=False)
plt.title("Feature Correlation Heatmap")
plt.show()

# STEP 8 — IDENTIFY TOP CORRELATED FEATURES
# Sort correlations with SalePrice in descending order

print(corr["SalePrice"].sort_values(ascending=False))

# STEP 9 — FINAL DATASET CHECK
print("Dataset shape:", df.shape)
print(df.head())
