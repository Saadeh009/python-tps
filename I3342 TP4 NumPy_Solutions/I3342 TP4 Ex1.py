# Consider the two-dimensional array, arr2d. 
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Write a code to slice this array to display the last column [[3], [6], [9]]
# Write a code to slice this array to display the last 2 elements of middle array [5 6]

import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

list1 = arr2d[:, -1:] # loop through all rows and include last element
print(list1)

list2 = arr2d[1, -2:] # loop through row of index 1 and include last 2 elements
print(list2)