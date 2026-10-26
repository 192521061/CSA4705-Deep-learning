import numpy as np

# Input matrix
X = np.array([[30, 60],
              [35, 70]])

# Weight matrix
W = np.array([[0.2, 0.5],
              [0.4, 0.3]])

# Matrix multiplication
Y = np.dot(X, W)

# Display predicted output
print("Predicted Output Matrix:")
print(Y)