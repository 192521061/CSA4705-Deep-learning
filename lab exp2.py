import numpy as np

# Input features and weights
X = np.array([4, 6, 8])
W = np.array([0.5, 0.3, 0.2])

# Bias
b = 2

# Calculate predicted output
Y = np.dot(X, W) + b

# Display the result
print("Predicted Output:", Y)