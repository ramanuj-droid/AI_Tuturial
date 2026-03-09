import numpy as np
import matplotlib.pyplot as plt
"""
np.random.seed(42)
x = np.random.rand(100) * 10

w  = 2
b = 4
y_pred = w * x + b

plt.scatter(x, y_pred)

plt.xlabel("X")
plt.ylabel("y")
plt.title("Regression Data")

"""

#MSE Calculation

y_pred = np.array([10,12,15,20])
y_act = np.array([9,10,14,19])

residual =  y_act - y_pred
mse =np.mean(residual **2)

#Comparing Models
"""
y_true = np.array([10,12,15])

model_A = np.array([9,11,14])
model_B = np.array([6,9,12])

mse_A = np.mean((y_true - model_A)**2)
mse_B = np.mean((y_true - model_B)**2)

if(mse_A > mse_B):
    print(mse_B," is better model")
else:
    print(mse_A," is better model")
"""
#GRADIENT DESCENT
np.random.seed(42)

X = np.random.rand(100) * 10
y = 4*X + 3 + np.random.randn(100)
w = 0
b = 0

learning_rate = 0.001
epochs = 1000

n = len(X)

for i in range(epochs):
    y_pred = w*X + b
    error = y_pred - y
    dw = (2/n) * np.sum(error * X)
    db = (2/n) * np.sum(error)

    w = w - learning_rate * dw
    b = b - learning_rate * db

print("Learned w:", w)
print("Learned b:", b)
plt.scatter(X,y)
y_final = w*X + b
plt.plot(X,y_final,color="red")

plt.show()