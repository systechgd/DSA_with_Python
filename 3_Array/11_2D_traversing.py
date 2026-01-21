########### Traversing of given 2D array ##########

import numpy as np

data =  [
    [22, 25, 21, 19],  #  > 0 row
    [23, 26, 22, 20],  #  > 1 row
    [21, 24, 20, 18]   #  > 2 row
]

arr1 = np.array(data)

for row in range(len(arr1)):
    for col in range(len(arr1[0])):
        print(arr1[row][col])

# Time Complexity  O(r*c)
# Space Complexity O(1)