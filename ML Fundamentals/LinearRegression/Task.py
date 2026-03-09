import numpy as np
import matplotlib.pyplot as plt
"""

Task 2 — Generate Synthetic Linear Data

Write Python code to generate:
y = 5x + 10 + noise
Plot the dataset.

Task 3 — Using the same dataset:Plot three lines:

y = 5x + 10
y = 3x + 2
y = 8x - 5

Observe which line fits best.

Task 4 — Multiple Feature Equation : Write a regression equation for predicting car price using:

engine_size
car_age
mileage

Write the full mathematical equation.

"""

"""
np.random.seed(42)

x = np.random.rand(100) * 10

y = 5 * x + 10 + np.random.randn(100)

# Different model lines
y_pred = 5 * x + 10
y_pred1 = 3 * x + 2
y_pred2 = 8 * x - 5

plt.scatter(x, y, label="Data")

plt.plot(x, y_pred, label="y = 5x + 10")
plt.plot(x, y_pred1, label="y = 3x + 2")
plt.plot(x, y_pred2, label="y = 8x - 5")

plt.legend()
plt.title("Linear Regression Lines")
plt.show()
"""

"""
np.random.seed(0)

engine_size = np.random.rand(100) * 2000
car_age = np.random.rand(100) * 10
mileage = np.random.rand(100) * 200000

w1 = 50
w2 = -2000
w3 = -0.05
b = 5000

price = w1*engine_size + w2*car_age + w3*mileage + b

plt.scatter(engine_size, price)
plt.xlabel("Engine Size")
plt.ylabel("Price")

plt.title("Car Price vs Engine Size")
plt.show()
"""
"""
Task 1 — Compute Residuals

Dataset:

Actual:      [20, 25, 30, 35]
Predicted:   [18, 28, 29, 36]

Find: Residuals,Squared residuals,MSE
Task 2 — Write Your Own MSE Function

Write a Python function:

def mse(y_true, y_pred):that returns mean squared error.

Task 3 — Model Comparison

Dataset:
Actual = [5,7,9,11]
Model A: [4,7,10,12]
Model B: [5,6,8,10]

Compute which model is better using MSE.

Task 4 — Plot Residuals
Generate synthetic regression data:

y = 4x + 3 + noise
Fit a random line:

y = 3x + 2
Plot:

• data points
• regression line
• vertical residual lines
"""
#TASK 1

y_pred = np.array([20,25,30,35])
y_act = np.array([18,28,29,36])

residual =  y_act - y_pred
mse =np.mean(residual **2)

#TASK 2

def mse(y_true,y_predicted):
    res = y_true - y_predicted
    return np.mean(res**2)

print(mse(y_act,y_pred))

#TASK 3

y_true = np.array([5,7,9,11])

model_A = np.array([4,7,10,12])
model_B = np.array([5,6,8,10])

mse_A = np.mean((y_true - model_A)**2)
mse_B = np.mean((y_true - model_B)**2)

if(mse_A > mse_B):
    print(mse_B," is better model")
else:
    print(mse_A," is better model")

#TASK 4

np.random.seed(42)

x = np.random.rand(100) * 10
y = 4*x + 3 + np.random.randn(100)
y_graph = 3*x + 2

plt.scatter(x,y,label="Data")

plt.plot(x,y_graph,color="red",label="Model")

for i in range(len(x)):
    plt.plot([x[i],x[i]],[y[i],y_graph[i]],color="gray")

plt.legend()
plt.show()