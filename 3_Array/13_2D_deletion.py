########### Deletion #######
# deleting elements from a 2D array does not happen “in place”
# NumPy creates a new array with the specified rows or columns removed

import numpy as np

data =  [
    [22, 25, 21, 19],  #  > 0 row
    [23, 26, 22, 20],  #  > 1 row
    [21, 24, 20, 18]   #  > 2 row
]

arr1 = np.array(data)

# Deletion Row
print(arr1, '\n')

arr1 = np.delete(arr1, 0, axis=0)
print(arr1, '\n')

# Delete Colum
arr1 = np.delete(arr1, 3, axis=1)
print(arr1)

# Time O(mn)
# Space O(mn)