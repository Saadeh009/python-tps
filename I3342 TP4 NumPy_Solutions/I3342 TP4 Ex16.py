# Replace all odd numbers in arr with -1 without changing arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# > array([ 0, -1, 2, -1, 4, -1, 6, -1, 8, -1])

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
new_array = np.where(arr % 2 == 1, -1, arr)

print(arr)
print(new_array)

# Syntax: np.where(condition, x, y)

# Parameters:
# condition: The condition that determines which elements to select from x and y.
#   It can be a boolean array or a condition that evaluates to a boolean array.
# x: The value to select when the condition is True.
# y: The value to select when the condition is False.

# Returns:
# An array with elements from x where the condition is True, and elements from y where the condition is False.