import matplotlib.pyplot as plt
import numpy as np
"""
x = np.array([1,2,3,4,5,7])
y = np.array([7,5,4,3,2,1])

plt.title("Sales Over Time")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.plot(x,y, marker="o",linestyle="--")
plt.grid(True)
plt.legend()

-   solid
--  dashed
:   dotted

o  circle
s  square
^  triangle
"""


#plt.savefig("chart.png")     Saving Images
"""
#Bar Charts

categories = ["IT","HR","Finance","Sales"]
employees = [50,30,20,40]

plt.bar(categories, employees)

plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

"""
"""
#Histogram

import numpy as np

data = np.random.randint(20,60,100)

plt.hist(data)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

"""
"""
#Scatterplot

age = [20,25,30,35,40]
salary = [30000,35000,45000,50000,60000]

plt.scatter(age, salary)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()
"""

"""
fig, axes = plt.subplots(1,2)

x = [1,2,3,4]
y = [10,20,25,30]

axes[0].plot(x,y)
axes[0].set_title("Line Plot")

axes[1].bar(["A","B","C"], [5,7,3])
axes[1].set_title("Bar Chart")

plt.show()
"""

