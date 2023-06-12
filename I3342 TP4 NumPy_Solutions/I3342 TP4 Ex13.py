# Get the positions where elements of two arrays match
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,9,2,7,4,9,4,9,8])
# Desired Output:
# > (array([1, 3, 5, 7]),)

import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 9, 2, 7, 4, 9, 4, 9, 8])
matches = np.where(a == b)
print(a)
print(b)
print(matches)