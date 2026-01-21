########### Insertion ###############

import array

my_array = array.array('i', [1,2,3,4])
print(my_array)

# insert element at begining all existing elments shift right     arr[0]   >>>>> 1 step right  
my_array.insert(0,6)
print(my_array)


# insert element at middle right elements shift 1 step right      arr[2]   >>>>> 1 step right
my_array.insert(2,6)
print(my_array)


# insert at last element , no shift
my_array.append(6)
print(my_array)

'''
| Operation         | Time Complexity | Space Complexity |
| ----------------- | --------------- | ---------------- |
| `print(my_array)` | O(n)            | O(1)             |
| `insert(0, 6)`    | O(n)            | O(1)             |
| `insert(2, 6)`    | O(n)            | O(1)             |
| `append(6)`       | O(1) amortized  | O(1)             |
'''