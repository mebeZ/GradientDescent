# -*- coding: utf-8 -*-
"""gradient-descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wxfs5Efvk9BmzfeGGCezPngyNnoZjF4-
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(100)
n = len(X)
noise = np.random.normal(loc=0, scale=10, size=100)
m = 1/2
b = 50
y = m*X + b + noise
y[y>100] = 100

plt.plot(X, y)

# Gradient descent
def grad_descent(n_steps=200, alpha=0.0002, beta=0.08): 
  losses = np.array([])
  params = np.array([0.0,0.0])

  for i in range(n_steps):
    # compute new line
    y_pred = params[0] * X + params[1]
    #print(f'y_pred {y_pred[:5]}')
    # compute loss
    loss = (1/n) * np.sum((y - y_pred) ** 2)
    #print(f'loss {loss}')
    #print(loss)
    losses = np.append(losses, loss)

    # compute gradient
    delta_m = (2/n) * np.sum(X * (y - y_pred)) * alpha
    delta_b = (2/n) * np.sum(y - y_pred) * beta
    grad = np.array([delta_m, delta_b]) 
    #print(f"+m: {grad[0]} +b {grad[1]}")
    # update params
    params = params + grad
    #print(f'm={params[0]} b={params[1]}')

  return params, losses

params, losses = grad_descent()
#print(losses)

plt.plot(np.arange(len(losses)), losses)
plt.show()

y_pred = params[0] * X + params[1]
plt.plot(X, y)
plt.plot(X, y_pred)
plt.show()