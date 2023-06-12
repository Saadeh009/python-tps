# Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and 
# on flattened array.
# Expected Output:
# Original array: [[10 40] [30 20]]
# Sort the array along the first axis:
# [[10 20] [30 40]]
# Sort the array along the last axis:
# [[10 40] [20 30]]
# Sort the flattened array:
# [10 20 30 40]

import numpy as np

# Define the original array
original_array = np.array([[10, 40], [30, 20]])

print("Original array:")
print(original_array)

# Sort the array along the first axis
sorted_first_axis = np.sort(original_array, axis=0)
print("\nSort the array along the first axis:")
print(sorted_first_axis)

# Sort the array along the last axis
sorted_last_axis = np.sort(original_array, axis=1)
print("\nSort the array along the last axis:")
print(sorted_last_axis)

# Sort the flattened array
sorted_flattened = np.sort(original_array.flatten())
print("\nSort the flattened array:")
print(sorted_flattened)