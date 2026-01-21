# Accessing elements

import numpy as np

data =  [
    [22, 25, 21, 19],  #  > 0 row
    [23, 26, 22, 20],  #  > 1 row
    [21, 24, 20, 18]   #  > 2 row
]

arr1 = np.array(data)
print(arr1, '\n')

# Accessing elements
def accessElement(arr, row, col):
    try:
        print(arr[row][col])
    except Exception as e:
        print(e)

accessElement(arr1, 0, 0)   # 22
accessElement(arr1, -1, -1) # 18
accessElement(arr1, 11, -1) # Index error


# Time Complexity O(1)
# Space Complexity O(1)
