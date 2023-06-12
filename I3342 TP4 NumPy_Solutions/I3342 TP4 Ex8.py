# Write a NumPy program to get true division of the element-wise array inputs.
# Use np.true_divide(x, 3): This line performs element-wise true division of x by 3.

import numpy as np

arr = np.array([10, 20, 30])
result = np.true_divide(arr, 3)
print(arr, result)