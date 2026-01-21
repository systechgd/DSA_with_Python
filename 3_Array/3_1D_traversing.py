########## Traversing Array ############
import array

arr1 = array.array('i', [1,2,3,4,5,6])
print(arr1)


# Traversing array

def traverseArray(arr):
    for i in arr:           # Time complexity O(n)
        print(i)            # Time complexity O(1)

traverseArray(arr1)

# Space complexity O(1)