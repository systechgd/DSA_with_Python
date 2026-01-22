############## Deletion #############
'''
📌 Key Considerations

1. Python lists are mutable → elements can be deleted.
2. Deleting single element shifts subsequent elements → O(n) time.
3. Deleting last element with pop() → O(1) (no shift required).
4. Deleting slice or multiple elements → O(n + k), depending on size.
5. Nested lists deletion depends on which level.
6. del, pop(), and remove() are the main methods.
7. remove(x) deletes first occurrence of value → O(n).
'''

# ============================================

# Delete by index

lst = [10, 20, 30, 40, 50]
print(f'Delete by index List: \n{lst}\n')

del lst[2]  # delete element at index 2
print(f'After Delete: \n{lst}\n')  # [10, 20, 40, 50]

# ✔️ Time: O(n) - Elements after index 2 are shifted left.
# ✔️ Space: O(1)

# ============================================

# Using pop()

lst = [10, 20, 30, 40, 50]
print(f'Using pop() List: \n{lst}\n')

last = lst.pop()
print(f'Using pop() deleted last element: \n{lst}\n')

removed = lst.pop(2)  # removes index 2
print(f'Using pop(2) removes index 2: \n{lst}\n')     # [10, 20, 40, 50]

# pop() last element → O(1)
# pop(i) → O(n) (elements shifted)

# ============================================

# Delete by Value

lst = [10, 20, 30, 40, 30]
print(f'Delete by Value List: \n{lst}\n')

lst.remove(30)  # removes first 30
print(f'Delete by Value List, remove element using lst.remove(30) : \n{lst}\n')      # [10, 20, 40, 30]

# Searches from start; deletes first occurrence only.

# ✔️ Time: O(n) 
# ✔️ Space: O(1)

# ============================================

# Delete Slice

lst = [10, 20, 30, 40, 50]
print(f'Delete by Slice List: \n{lst}\n')

del lst[1:4]  # delete indices 1,2,3
print(f'Delete by Slice List, del lst[1:4] : \n{lst}\n')    # [10, 50]

# ✔️ Time: O(n) 
# ✔️ Space: O(1)
# Shifts elements after the slice.

# ============================================

# Delete All Elements / Clear List
lst = [10, 20, 30]
lst.clear()
print(lst)  # []

# ✔️ Time: O(n) - each reference removed
# ✔️ Space: O(1) - list now empty, objects freed if no other references
# Shifts elements after the slice.

# ============================================

'''
| Deletion Type       | Method                     | Time Complexity | Space Complexity | Notes               |
| ------------------- | -------------------------- | --------------- | ---------------- | ------------------- |
| Last element        | `pop()`                    | O(1)            | O(1)             | Fastest deletion    |
| Arbitrary index     | `pop(i)` / `del lst[i]`    | O(n)            | O(1)             | Elements shifted    |
| By value            | `remove(x)`                | O(n)            | O(1)             | Deletes first match |
| Slice               | `del lst[i:j]`             | O(n)            | O(1)             | Shifts remaining    |
| All elements        | `clear()`                  | O(n)            | O(1)             | Empties list        |
| Nested list element | `del nested[i][j]`         | O(m)            | O(1)             | m = inner list size |
| Conditional         | `[x for x in lst if cond]` | O(n)            | O(n)             | Creates new list    |
'''
