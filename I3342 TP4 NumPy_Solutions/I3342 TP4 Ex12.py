# Create the following pattern without hardcoding. Use only numpy functions
# a = np.array([1,2,3])
# > array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

import numpy as np

a = np.array([1, 2, 3])
pattern = np.concatenate([np.repeat(a, 3), np.tile(a, 3)])
print(pattern)

# np.repeat(a, 3) returns [1, 1, 1, 2, 2, 2, 3, 3, 3]
# np.tile(a, 3)   returns [1, 2, 3, 1, 2, 3, 1, 2, 3]