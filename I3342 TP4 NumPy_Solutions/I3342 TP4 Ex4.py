# Write a NumPy program to compute the determinant of a given square array.

import numpy as np

matrixA = np.array([[1, 2], [3, 4]])
detA = np.linalg.det(matrixA)
print(matrixA, detA)

matrixB = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
detB = np.linalg.det(matrixB)
print(matrixB, detB)