# 1. Create an array of 10 zeros.
# 2. Create an array with values between 10 and 49
# 3. Reverse an array
# 4. Find the index of the non zeros elements of this array [1,2,0,0,4,0]
# 5. Create a matrix of size 8x8 – fill the matrix with values 0 or 1 as a chess table.
# 6. Create a matrix of size 5x5 where rows values vary between 0 and 4
# 7. Create a random vector of size 10. Replace the maximum value by 0.
# 8. In an array, Find the element close to a certain value.

import numpy as np

print("1- array of 10 zeros:")
list1 = np.zeros(10, dtype=int)
print(list1)

print("\n2- array with values between 10 and 49:")
list2 = np.arange(10,50)
print(list2)

print("\n3- reversed array:")
list3 = np.flip(list2)
print(list3)

print("\n4- index of the non zeros elements of this array [1,2,0,0,4,0]:")
list4 = np.array([1, 2, 0, 0, 4, 0])
nonzero_indices = np.nonzero(list4)
print(nonzero_indices)

print("\n5- matrix of size 8x8 with values 0 or 1 as a chess table:")
list5 = np.zeros((8, 8), dtype=int) # create 8x8 array of zeros
list5[1::2, ::2] = 1 # replace elements with 1 if needed
list5[::2, 1::2] = 1
print(list5)

print("\n6- matrix of size 5x5 where rows values vary between 0 and 4:")
list6 = np.tile(np.arange(5), (5, 1))
print(list6)

print("\n7- random vector of size 10. Replace the maximum value by 0:")
list7 = (np.random.rand(10) * 100).astype(int)
print("before replacing:", list7)
max_value = np.max(list7)
print("max value:", max_value)
list7[list7 == max_value] = 0
print("after replacing:", list7)

print("\n8- element close to a certain value in an array:")
list8 = np.array([1, 3, 5, 7, 9])
target_value = 6
closest_element = list8[np.argmin(np.abs(list8 - target_value))]
print(list8)
print("target value:", target_value)
print("closest value:", closest_element)

# functions used:
# np.zeros(): This function creates an array filled with zeros.
# The function takes the desired shape of the array as an argument and returns the array.

# np.arange(): This function creates an array with a sequence of values within a specified range.
# It takes the start, stop, and step size as arguments and returns an array containing the values.

# np.flip(): This function reverses the order of elements in an array along a specified axis.
# By default, it reverses the array along all axes. It returns the reversed array.

# np.nonzero(): This function returns the indices of the non-zero elements in an array.
# It takes an array as an argument and returns a tuple of arrays, each representing the indices along a different axis.

# np.tile(): This function constructs an array by repeating a given array or a sequence of values.
# It takes the array to be tiled and the number of repetitions along each axis as arguments and returns the tiled array.

# np.random.rand(): This function generates random numbers from a uniform distribution over the interval [0, 1).
# It takes the desired shape of the random array as an argument and returns the array.

# np.max(): This function returns the maximum value in an array or along a specified axis.
# It takes the array as an argument and returns the maximum value.

# np.argmin(): This function returns the indices of the minimum values in an array or along a specified axis.
# It takes the array as an argument and returns the index of the minimum value.

# np.abs(): This function returns the absolute value of each element in an array.
# It takes the array as an argument and returns the array with absolute values.