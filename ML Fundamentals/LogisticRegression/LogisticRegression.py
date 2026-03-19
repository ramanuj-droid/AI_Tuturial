import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-10,10,100)
y = sigmoid(z)

plt.plot(z,y)
plt.title("Sigmoid Function")

def binary_cross_entropy(y_true, y_pred):
    
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    
    loss = -np.mean(
        y_true * np.log(y_pred) +
        (1 - y_true) * np.log(1 - y_pred)
    )
    
    return loss

np.random.seed(42)

X = np.random.randn(200,1)
y = (X > 0).astype(int)

w = np.zeros((1,1))
b = 0

learning_rate = 0.1
epochs = 1000

loss_history = []

n = X.shape[0]

for i in range(epochs):
    z = X @ w + b

    y_pred = sigmoid(z)
    loss = binary_cross_entropy(y, y_pred)
    loss_history.append(loss)

    dw = (1/n) * (X.T @ (y_pred - y))
    db = (1/n) * np.sum(y_pred - y)

    w = w - learning_rate * dw
    b = b - learning_rate * db

print("Weight:", w)
print("Bias:", b)

y_pred_prob = sigmoid(X @ w + b)
y_pred_class = (y_pred_prob >= 0.5).astype(int)

accuracy = np.mean(y_pred_class == y)
print("Accuracy:", accuracy)

plt.plot(loss_history)
plt.title("Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()