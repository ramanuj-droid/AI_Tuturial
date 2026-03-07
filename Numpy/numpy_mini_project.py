#LINEAR REGRESSION

"""

| Size (sqft) | Price |
| ----------- | ----- |
| 1000        | 200   |
| 1500        | 300   |
| 2000        | 400   |
| 2500        | 500   |

y = mx + b
m → slope (weight)
b → bias

"""
import numpy as np

x = np.array([1000,1500,2000,2500])
y = np.array([200,300,400,500])

X = x.reshape(-1,1)

X = X / 1000

m = 0
b = 0

lr = 0.01
epochs = 1000

for i in range(epochs):

    y_pred = m * X + b

    error = y_pred - y.reshape(-1,1)

    dm = (2/len(X)) * np.sum(error * X)
    db = (2/len(X)) * np.sum(error)

    m = m - lr * dm
    b = b - lr * db

print("Slope:", m)
print("Intercept:", b)

size = 1800/1000

prediction = m * size + b

print("Predicted price:", prediction)