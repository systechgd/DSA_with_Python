############# Creation List #####################
'''
## Notation Used
n :	Number of elements in the list
k :	Number of elements inside a nested list
d :	Depth of nesting (levels)
'''


# List of Integers
int_list = [10, 20, 30, 40, 50, 60]
print(f'Integer List: \n{int_list}\n')

# Time Complexity O(n)
# Space Complexity O(n)
# Explanation : Allocate n references

#------------------------------------------

# List of String
string_list = ['web1', 'web2', 'db1', 'proxy']
print(f'String List: \n{string_list}\n')

# Time Complexity O(n)
# Space Complexity O(n)
# Explanation : Store references to string object

#------------------------------------------


# Mixed List
mixed_list = [
    10,                         # int
    3.14,                       # float
    2 + 5j,                     # complex
    True,                       # boolean
    "Hello",                    # string
    None,                       # NoneType
    [1, 2, 3],                  # list
    (4, 5, 6),                  # tuple
    {7, 8, 9},                  # set
    {"name": "Alice", "age": 25},  # dictionary
    b"ABC",                     # bytes
    range(5)                    # range
]
print(f'Mixed List: \n{mixed_list}\n')

# Time Complexity O(n)
# Space Complexity O(n)
# Explanation : Heterogeneous types do not affect complexity

#------------------------------------------

# Mixed Nested list
mixed_nested = [
    [1, 2.5, "A"],
    ["Hello", True, None],
    [10, [20, 30], 40]
]
print(f'Mixed Nested List: \n{mixed_nested}\n')

# Outer Level List
# Time Complexity O(n)
# Space Complexity O(n)
# Explanation : n = number of sublists

# Inner Level lists
# Time Complexity O(k)
# Space Complexity O(k)
# Explanation : Each inner list stores k elements

# Total Complexity for nested lists
# Total Time	O(n + Σk)
# Total Space	O(n + Σk)
# Σk = total elements across all nested lists
# The symbol Σ (capital Greek letter Sigma) means 'summation'.