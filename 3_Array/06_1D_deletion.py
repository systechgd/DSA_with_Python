####### Element Deletion in Array ###########

# when you delete elements all right side elements shift one position to left <<<<

from array import *

arr1 = array('i', [1,2,3,4,5,6,7])
print(arr1)

# remove first element
arr1.remove(1)  # remove element
print(arr1)

# remove last element ,  Time Complexity O(1)
arr1.pop()
print(arr1)

# remove element with index number,
arr1.pop(1)
print(arr1)


# Time Complexity O(n)
# Space complexity O(1)
