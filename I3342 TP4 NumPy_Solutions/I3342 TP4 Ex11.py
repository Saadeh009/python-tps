# Extract all odd numbers from an array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_numbers = arr[arr % 2 != 0]
print(odd_numbers)