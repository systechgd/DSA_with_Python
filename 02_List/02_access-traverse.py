############# Accessing and Traversing through list ###########
'''
📌 Key Considerations (Must Know)
1. Python lists are indexed (0-based)
2. Support positive & negative indexing
3. Accessing an element is O(1)
4. Traversal always takes O(n)
5. Lists can be nested
6. Traversal does not create a copy (unless you slice)
'''

# 1️⃣ accessing list
## Positive indexing
lst = [10, 20, 30, 40, 50]
print(lst[0]) # 10
print(lst[2]) # 30

## Negative indexing
print(lst[-1]) # 50 last element
print(lst[-2]) # 40

# ✔️ Time Complexity: O(1)
# ✔️ Space Complexity: O(1)

#-----------------------------------------------------------------------------------

# 2️⃣ Accessing Sublist (Slicing)
print(lst[1:4]) # [20, 30, 40] , 4th excluded
print(lst)

print(lst[:3]) # [10, 20, 30] 
print(lst[2:]) # [30, 40, 50]
print(lst[::-1]) # reverse [50, 40, 30, 20, 10]
print(lst[::2]) # 2 steps [10, 30, 50]

# ✔️ Time: O(k)
# ✔️ Space: O(k)
# slicing create a new list

#-----------------------------------------------------------------------------------

# 3️⃣ Traversing List 

for item in lst:
    print(item)

# ✔️ Time: O(n)
# ✔️ Space: O(1)

# ============================================

# Using index with range()
for i in range(len(lst)):
    print(f'Index: {i}, Value: {lst[i]}')

# Useful when index is needed

# ============================================

# Using while loop

count = 0
while count < len(lst):
    print(lst[count])
    count += 1

# ============================================

# Traversing with Index & Value
for idx, value in enumerate(lst):
    print(f'Index: {idx}, Value: {value}')

# Best practice when both are needed

# ============================================

# 4️⃣ Traversing a Nested List
nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing Nested Elements

print(nested[1][1]) # 5

# Traversing nested list

for row in nested:
    for val in nested:
        print(row, val)

# ✔️ Time: O(n × m)
# ✔️ Space: O(1)

# ============================================

# 5️⃣ Mixed nested list
mixed_nested = [
    [1, 2.5, "A"],
    ["Hello", True, None],
    [10, [20, 30], 40]
]

# accessing mixed nested list
print(mixed_nested[2][1][0]) # 20

# Traversing mixed nested list
for item in mixed_nested:
    for sub in mixed_nested:
        print(sub)

'''
| Operation            | Time     | Space  |
| -------------------- | -------- | ------ |
| Access element       | `O(1)`   | `O(1)` |
| Slice access         | `O(k)`   | `O(k)` |
| Traverse list        | `O(n)`   | `O(1)` |
| Traverse nested list | `O(n×m)` | `O(1)` |
'''