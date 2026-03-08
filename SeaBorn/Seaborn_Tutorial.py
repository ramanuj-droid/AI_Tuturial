"""
Seaborn is built on top of Matplotlib but provides better default visuals and statistical plots.
Used heavily in:

data analysis notebooks
ML feature analysis
detecting outliers
class imbalance analysis

"""

import matplotlib.pyplot as plt
import seaborn as sns

#tips is a random dataset in seaborn
df = sns.load_dataset("tips")

#Count Plot : Shows category frequency.
"""
sns.countplot(x="day", data=df)
plt.title("Number of Customers per Day")
plt.show()
"""
#Distribution Plot (Histogram + KDE) : Shows data distribution.
"""
sns.histplot(df["total_bill"], kde=True)
plt.title("Total Bill Distribution")
plt.show()
"""
#Box Plot (Outlier Detection) : reveal: median,quartiles,outliers,spread
"""
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Bill Distribution by Day")
plt.show()
"""
#Scatter Plot with Seaborn : Shows relationships between variables.

"""
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Bill vs Tip Relationship")
plt.show()
"""

#Pairplot : Pairplot shows relationships between all numerical variables.

sns.pairplot(df)
plt.title("total_bill vs tip correlation")
plt.show()

#Correlation Matrix : Correlation measures linear relationship between variables.
"""
Values range:

-1 → strong negative correlation
0 → no correlation
+1 → strong positive correlation


corr = df.corr(numeric_only=True)
print(corr)
"""

#Heatmap : Heatmap visualizes the correlation matrix.

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

#Advance Plot

#Heatmap : Heatmap visualizes the correlation matrix.

"""
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
"""

"""
df = sns.load_dataset("tips")
plt.figure(figsize=(8,5))
sns.histplot(df["total_bill"])
plt.title("Total Bill Distribution")
plt.show()
"""
#Styles
sns.set_style("whitegrid")

#Available styles: white,dark,whitegrid,darkgrid,ticks

"""
sns.set_style("darkgrid")
sns.histplot(df["total_bill"])
plt.show()
"""
#Color Palettes : Use consistent colors.

#sns.countplot(x="day", data=df, palette="Set2")

#Common palettes: Set1,Set2,coolwarm, viridis,pastel

sns.boxplot(x="day", y="total_bill", data=df, palette="Set3")

# Multiple Plots in One Figure

"""
fig, axes = plt.subplots(1,2, figsize=(12,5))
sns.histplot(df["total_bill"], ax=axes[0])
axes[0].set_title("Bill Distribution")

sns.boxplot(x="day", y="total_bill", data=df, ax=axes[1])
axes[1].set_title("Bills by Day")

plt.show()
"""
#Annotations (Highlight Important Points)
"""
plt.figure(figsize=(8,5))
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Bill vs Tip")

plt.annotate(
    "High Bill",
    xy=(50,10),
    xytext=(35,12),
    arrowprops=dict(facecolor="black")
)
plt.show()
"""