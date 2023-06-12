# Write a NumPy program to concatenate element-wise two arrays of string.
# Array1:['Python' 'PHP']
# Array2:[' Java' ' C++']
# new array: ['Python Java' 'PHP C++']

import numpy as np

arr1 = np.array(['Python', 'PHP'])
arr2 = np.array([' Java', ' C++'])
arr3 = np.char.add(arr1, arr2)

print("Array1:", arr1)
print("Array2:", arr2)
print("New array:", arr3)