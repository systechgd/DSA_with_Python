########## create 2D array ###############
# Create a 2D array to create metrix

import numpy as np

temperature = [
#col 0   1    2   3
    [22, 25, 21, 19],  #  > 0 row
    [23, 26, 22, 20],  #  > 1 row
    [21, 24, 20, 18]   #  > 2 row
]

twoD = np.array(temperature)
print(twoD)

# Access elements from 2D array
print(twoD[0][0])       # first element
print(twoD[2][3])       # last element


"""
`np.array(temperature)` 
Time complexity : O(rows × cols) = O(n × m) 
Space complexity : O(rows × cols) = O(n × m) 
Copies data into NumPy’s contiguous memory 
rows = 3, cols = 4, so here O(12)
NumPy arrays store all elements in contiguous memory, unlike Python lists of lists


`twoD[i][j]` or `twoD[i,j]`
Time Complexity : O(1)
Space Complexity : O(1)
Direct index access, constant time

Accessing any element in a NumPy array is O(1) because it is stored in contiguous memory
Same complexity for updates: twoD[1,2] = 99 is O(1)
"""