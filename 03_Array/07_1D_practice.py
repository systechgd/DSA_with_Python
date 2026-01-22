#### initial setup ######
from array import *

arr = array('i', [])    # empty array


# 1️⃣ Create an array & Traverse

# creating array with element 
arr = array('i', [1,2,3,4,5,6])
print(arr)
'''
# traversing through array
for i in arr:
    print(i)

# Time: O(n)
# Space: O(1)
# Traversal visits every element
'''


'''
# 2️⃣ Access individual elements via index
print(arr[2]) # access element with index value
print(arr[0])

# Time: O(1)
# Space: O(1)
# Direct memory access
'''

'''
# 3️⃣ Insert element at end using append()
arr.append(7)
print(arr)

# Time: O(1) amortized
# Space: O(1)
# Resize happens occasionally
'''


'''
# 4️⃣ Insert element at beginning / middle using insert()
arr.insert(0, 11)    # begining
print(arr)
arr.insert(4,15)    # middle
print(arr)

# Time: O(n)
# Space: O(1)
# Shifting required
'''


'''
# 5️⃣ Extend array using extend()
arr.extend([7,8,9])
print(arr)

# Time: O(k) (k = elements added)
# Space: O(1)
# Copies new elements
'''


'''
# 6️⃣ Add items from list using fromlist()
arr.fromlist([10, 11])
print(arr)


# Time: O(k)
# Space: O(1)
# Similar to extend()
'''


'''
# 7️⃣ Remove element using remove()
arr.remove(3)
print(arr)


# Time: O(n)
# Space: O(1)
# Search + shift
'''


'''
# 8️⃣ Remove element using pop()
arr.pop()       # last
print(arr)

arr.pop(2)      # middle
print(arr)


# | Case     | Time   | Space  |
# | -------- | ------ | ------ |
# | `pop()`  | `O(1)` | `O(1)` |
# | `pop(i)` | `O(n)` | `O(1)` |
'''


'''
# 9️⃣ Access index of element using index()
print(arr.index(4))

# Time: O(n)
# Space: O(1)
# Linear search
'''


'''
# 🔟 Reverse array using reverse()
arr.reverse()
print(arr)


# Time: O(n)
# Space: O(1)
# In-place reversal
'''

'''
# 1️⃣1️⃣ Get buffer info using buffer_info()
print(arr.buffer_info())


# Time: O(1)
# Space: O(1)
# Returns (memory_address, length)
'''


'''
# 1️⃣2️⃣ Count occurrences using count()
print(arr.count(2))


# Time: O(n)
# Space: O(1)
# Full scan required
'''


'''
# 1️⃣3️⃣ Convert array to bytes using tostring() ⚠️ (deprecated)
print(arr.tobytes())

# Time: O(n)
# Space: O(n)
# Creates new bytes object
'''


'''
# 1️⃣4️⃣ Convert array to Python list using tolist()
print(arr.tolist())


# Time: O(n)
# Space: O(n)
# New list created
'''

'''
# 1️⃣5️⃣ Slice elements from array
print(arr[1:4])


Time: O(k)
Space: O(k)
Creates new array
'''

'''
# 1️⃣6️⃣ Reverse array using slicing
print(arr[::-1])


Time: O(n)
Space: O(n)
New reversed copy
'''