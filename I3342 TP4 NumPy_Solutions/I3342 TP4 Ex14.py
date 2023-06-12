# Write a NumPy program to create a structured array from given student name, height, 
# class and their data types. Now sort the array on height.
# Original array:[(b'James', 5, 48.5 ) (b'Nail', 6, 52.5 ) (b'Paul', 5, 42.1 ) (b'Pit', 5, 40.11)]
# Sorted by height: [(b'Pit', 5, 40.11) (b'Paul', 5, 42.1 ) (b'James', 5, 48.5 ) (b'Nail', 6, 52.5 )]
# Use np.sort()

import numpy as np

arr = np.array([(b'James', 5, 48.5), (b'Nail', 6, 52.5), (b'Paul', 5, 42.1), (b'Pit', 5, 40.11)])
arr_sorted = arr[np.argsort(arr[:, 2])]

print("Original array:")
print(arr)
print("Sorted by height:")
print(arr_sorted)