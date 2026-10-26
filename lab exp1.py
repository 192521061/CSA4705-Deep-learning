import numpy as np

# Create a 3x3 image matrix
A = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# Flatten the matrix into a 1D vector
vector = A.flatten()

# Calculate the total pixel intensity
total = np.sum(A)

# Display the results
print("Original Image Matrix:")
print(A)

print("Flattened Vector:")
print(vector)

print("Total Pixel Intensity:", total)