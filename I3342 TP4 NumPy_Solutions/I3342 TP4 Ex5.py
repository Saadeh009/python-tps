# Write a NumPy program to compute the outer product of two given vectors.

import numpy as np

p = np.array([[1, 0], [0, 1]])
q = np.array([[1, 2], [3, 4]])
outer_product = np.outer(p, q)

print(outer_product)