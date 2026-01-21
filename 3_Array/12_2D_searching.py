############# Searching 2D Array

import numpy as np

data =  [
    [22, 25, 21, 19],  #  > 0 row
    [23, 26, 22, 20],  #  > 1 row
    [21, 24, 20, 18]   #  > 2 row
]

arr1 = np.array(data)

##### Searching Element
def searchElement(arr, target):

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return f'Value presenet at index of : arr1[{i}][{j}]'
            
    return f'Value Not Presenet in given array'

print(searchElement(arr1, '200'))

# Time complexity O(r×c)
# Space complexity O(1)