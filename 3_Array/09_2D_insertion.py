######## Insertion ############
'''
❌ NumPy arrays:
Have fixed size
Require uniform shape
Do not support row-wise resizing
'''

import numpy as np

data =  [
    [22, 25, 21, 19],  #  > 0 row
    [23, 26, 22, 20],  #  > 1 row
    [21, 24, 20, 18]   #  > 2 row
]

arr1 = np.array(data)
print(arr1, '\n')

# Creating numpy array 
# Time	O(r × c)
# Space	O(r × c)

# insertion
# axis 0 = row
# axis 1 = col
# np.insert(arr, position, elements, axis)

# inserting new row at 1st index in metrix
newArr = np.insert(arr1, 1, [51, 52, 53, 54], axis=0)
print(newArr, '\n')

# Insertion Time complexity
# Copy elements before index	O(r × c)
# Copy inserted row	O(c)
# Copy elements after index	O(r × c)
# Total	O(r × c)

# insertion space complexity
# New NumPy array	O((r+1) × c)
# Extra temporary memory	O(1)
# Total	O(r × c)


# replace specific element
newArr[1][3] = 64
print(newArr)

# Time	O(1)
# Space	O(1)