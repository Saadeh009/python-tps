# Write a NumPy program to compute the median of flattened given array.
# The median is the value separating the higher half from the lower half 
# of a data sample (a population or a probability distribution). For a data set, it may be 
# thought of as the "middle" value. For example, in the data set {1, 3, 3, 6, 7, 8, 9}, the 
# median is 6, the fourth largest, and also the fifth smallest, number in the sample. For a 
# continuous probability distribution, the median is the value such that a number is equally 
# likely to fall above or below it.
# Original array:
# [[ 0 1 2 3 4 5]
# [ 6 7 8 9 10 11]]
# Median of said array:5.5

import numpy as np

arr = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11]])

flattened_arr = arr.flatten()
median = np.median(flattened_arr)

print("Original array:")
print(arr)
print("Flattened array:")
print(flattened_arr)
print("Median of the flattened array:", median)