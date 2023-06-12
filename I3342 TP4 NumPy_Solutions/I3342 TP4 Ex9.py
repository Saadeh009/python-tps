# Write a NumPy program to get the powers of an array values element-wise.
# Note: First array elements raised to powers 3.

import numpy as np

arr = np.array([2, 3, 4])
result = np.power(arr, 3)
print(arr, result)