############## Update List ###########
'''
📌 Key Considerations
1. Python lists are mutable → elements can be changed.
2. Updating a single element is O(1).
3. Updating multiple elements or slices is O(k) (number of elements updated).
4. Inserting/appending:
5. At the end (append) → O(1) amortized
6. At arbitrary positions → O(n) (shifts elements)
7. Python lists store references to objects.
8. Nested lists can be updated using multiple indices.
'''

#-----------------------------------------------------------------------------------
# 1️⃣ Updating Elements

# Update Single Element
lst = [10, 20, 30, 40, 50]
print(lst)

lst[2] = 35
print(f'\nUpdated List:\n{lst}\n')

# ✔️ Time: O(1)
# ✔️ Space: O(1)
# Update single element

# ============================================

# Update Multiple Elements (Slice)
lst[1:4] = [21, 36, 41]
print(f'Updated Multiple Elements:\n{lst}\n')

# ✔️ Time: O(k)
# ✔️ Space: O(k)
# Update slice of length k

# ============================================

# Update nexted list element
nested = [[1, 2], [3, 4], [5, 6]]
print(f'Nested list: \n{nested}\n')

nested[1][0] = 33
print(f'Updated nested element:\n{nested}\n')  # [[1, 2], [33, 4], [5, 6]]

# Single element update = O(1)

# ============================================

# Update with Loops or Conditions
lst = [10, 20, 30, 40, 50]
print(f"Loop List: \n{lst}\n")

for i in range(len(lst)):
    if lst[i] > 25:
        lst[i] +=5
print(f'updated list with loop: \n{lst}\n')

# ✔️ Time: O(n)
# ✔️ Space: O(1)


#-----------------------------------------------------------------------------------
# 2️⃣ Insertion Elements

print(f'\n Insertion ELements\n')

# Append (At End)
lst = [10, 20, 30]
print(f'Before append list: \n{lst}\n')

lst.append(40)
print(f'After append: \n{lst}\n')  # [10, 20, 30, 40]

# ✔️ Time: O(1) amortized
# ✔️ Space: O(1) (Python may resize array internally)


# ============================================

# Insert at Arbitrary Position

lst = [10, 20, 30, 40]
print(f'Before insert arbitory: \n{lst}\n')

lst.insert(2, 25)  # Insert 25 at index 2
print(f'After insert arbitory: \n{lst}\n')  # [10, 20, 25, 30, 40]

# ✔️ Time: O(n) elements shifted right
# ✔️ Space: O(1) 

# ============================================

# Extend / Concatenate Lists

lst1 = [1, 2, 3]
lst2 = [4, 5]
print(f'Before Extend: \n{lst1}\n')

lst1.extend(lst2)
print(f'After Extend: \n{lst1}\n')  # [1, 2, 3, 4, 5]

# ✔️ Time: O(k) → k = length of added list
# ✔️ Space: O(k) → references copied

# ============================================

# Insert in Nested List

nested = [[1, 2], [3, 4]]
print(f'Before insert nested list: \n{nested}\n')

nested[1].insert(1, 33)
print(f'After insert nested list: \n{nested}\n') # [[1, 2], [3, 33, 4]]

# ✔️ Time: O(m) → m = number of elements in inner list


#-----------------------------------------------------------------------------------
'''
| Operation             | Method                   | Time Complexity | Space Complexity |
| --------------------- | ------------------------ | --------------- | ---------------- |
| Update single element | `lst[i] = x`             | O(1)            | O(1)             |
| Update slice          | `lst[i:j] = [...]`       | O(k)            | O(k)             |
| Append at end         | `lst.append(x)`          | O(1) amortized  | O(1)             |
| Insert at index       | `lst.insert(i, x)`       | O(n)            | O(1)             |
| Extend list           | `lst.extend(lst2)`       | O(k)            | O(k)             |
| Insert in nested list | `nested[i].insert(j, x)` | O(m)            | O(1)             |
'''