########## Craeting Array ###################


########### using array module only allow us to create homegenous data

import array

# integer empty array, Time & Space complexity O(1) 
my_array = array.array('i')
print(my_array)

# array with elements, Time & Space complexity O(n)
my_array = array.array('i', [1,2,3,4])
print(my_array)




############ using numpy module, we can create hetrogenous array
import numpy as np

# create empty array , Time & Space complexity O(1)
np_array = np.array([], dtype=int)
print(np_array)

# Create with element, Time & Space complexity O(n)
np_array = np.array([1,2,3,4,5])
print(np_array)
