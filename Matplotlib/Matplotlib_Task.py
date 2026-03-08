import matplotlib.pyplot as plt

"""
Practice Tasks
Task 1 : Create a bar chart:

Departments: IT, HR, Sales
Employees: 40, 25, 35
Task 2 :Create a histogram for:

ages = [22,23,25,30,35,40,45,50]
Task 3 : Create a scatter plot:

x = [1,2,3,4,5]
y = [2,4,5,4,5]
Task 4 : Create two subplots:

left → line chart
right → bar chart"""
"""

"""

"""
Department = ["IT","HR","Sales"]
Employees = [40,25,35]

plt.xlabel("Department")
plt.ylabel("Employees")

plt.bar(Department,Employees)
plt.show()
"""
"""
ages = [22,23,25,30,35,40,45,50]
plt.hist(ages)
"""

x = [1,2,3,4,5]
y = [2,4,5,4,5]

plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x,y)

plt.show()