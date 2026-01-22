############ Accessing Array Elements ##########

from array import *

arr1 = array('i', [1,2,3,4,5,6,7])

# Accessing Array Elements
def accessElements(arr, idx):
    print('Index out of array') if idx >= len(arr) else print(arr[idx])

accessElements(arr1, 7)

# if idx >= len(arr)  >>>>>>>>>>> Time = O(1)
# print(arr[idx])     >>>>>>>>>>> Time = O(1)
# print('Index out of array')     >>>>>>>>>>> Time = O(1)
# Space = O(1), No extra space required
