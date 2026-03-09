"""
Build a Linear Regression model class with:

1) initialization
2) training (fit)
3) prediction (predict)
4) loss tracking

MODEL STRUCTURE

Model
 ├── fit()      → training
 ├── predict()  → inference
 └── parameters → weights & bias

 Output

 Prediction
Loss computation
Gradient calculation
Parameter updates
Training loop
"""
#Scalar Form

import numpy as np
import matplotlib.pyplot as plt

"""
class LinearRegression:
    def __init__(self, learning_rate = 0.001,epochs = 1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.w = None
        self.b = None
        self.loss_history = []
    
    def fit(self , x, y):
        n = len(x)
        self.w = 0
        self.b = 0
        for i in range(self.epochs):
            y_pred = self.w * x + self.b
            err = y_pred - y
            dw = (2/n) * np.sum(err * x)
            db = (2/n) * np.sum(err)

            self.w = self.w - self.lr * dw
            self.b = self.b - self.lr * db

            loss = np.mean(err*2)
            self.loss_history.append(loss)
    def predict(self,x):
        return self.w * x + self.b

np.random.seed(42)

X = np.random.rand(100) * 10
y = 7 * X + 5 + np.random.randn(100)

model = LinearRegression(
    learning_rate=0.001,
    epochs=1000
)

model.fit(X, y)

print("Learned weight:", model.w)
print("Learned bias:", model.b)
y_pred = model.predict(X)

plt.scatter(X, y, label="Data")
plt.plot(X, y_pred, color="red", label="Model")

plt.legend()
plt.show()

plt.plot(model.loss_history)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")

plt.show()
"""
#Vector Form

np.random.seed(42)

X = np.random.rand(100,1) * 10
y = 4 * X + 3 + np.random.randn(100,1)

w = np.zeros((1,1))
b = 0

learning_rate = 0.001
epochs = 1000

loss_history = []
n = X.shape[0]

for i in range(epochs):

    y_pred = X @ w + b
    error = y_pred - y
    dw = (2/n) * (X.T @ error)
    db = (2/n) * np.sum(error)
    w = w - learning_rate * dw
    b = b - learning_rate * db
    loss = np.mean(error**2)
    loss_history.append(loss)


print("Learned Weight:", w)
print("Learned Bias:", b)

y_final = X @ w + b
plt.scatter(X, y, label="Data")

plt.plot(X, y_final, color="red", label="Regression Line")

plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression (Vectorized)")

plt.legend()
plt.show()

plt.plot(loss_history)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Curve")

plt.show()