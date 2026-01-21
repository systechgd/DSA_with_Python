############ Searching Element in Array ##############
# Performed Linear search, check element one by one in increament fashion

from array import *

arr1 = array('i', [1,2,3,4,5,6,7,8,9])

def searchElement(arr, target):
    for i in range(len(arr)):       # Time Complexity O(n)
        if arr[i] == target:        # Time Complexity O(1)
            return i    # return index # Time O(1)
    return -1    # Not found element in array # Time O(1)

print(searchElement(arr1, 10))

# Time Complexity O(n)
# Space Complexity O(1), additional memory not required
# range function # Time Complexity O(1)