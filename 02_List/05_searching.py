############## Searching ###################

'''
📌 Key Considerations

1. Python lists are unsorted by default → searching requires linear scan.
2. Index-based search (index()) finds first occurrence.
3. Membership check (in) is a common Pythonic method.
4. Searching nested lists requires nested loops or comprehensions.
5. Binary search only works if the list is sorted.
6. Searching is O(n) for unsorted lists, O(log n) for sorted + binary search.
7. Lists store references → comparison uses object equality.
'''

# 1️⃣ Search Using in (Membership Test)

lst = [10, 20, 30, 40, 50]

print(20 in lst)  # True
print(25 in lst)  # False

# ✔️ Time: O(n) 
# ✔️ Space: O(1)
# Linear Scan

# ============================================

# 2️⃣ Search Using index()

lst = [10, 20, 30, 20, 50]

print(lst.index(20))  # 1 (first occurrence)
# print(lst.index(25))  # ValueError if not found

# ✔️ Time: O(n) 
# ✔️ Space: O(1)
# Linear search, first occurrence

# ============================================

# 3️⃣ Search in Nested Lists

nested = [[1, 2], [3, 4], [5, 6]]

# Search for 4
found = False
for row in nested:
    if 4 in row:
        found = True
        break
print(found)  # True

# Complexity: O(n × m)
# n = number of sublists
# m = average elements per sublist

# ============================================

# 4️⃣ Search Using Loop

lst = [10, 20, 30, 40]

for i, val in enumerate(lst):
    if val == 30:
        print(f"Found at index {i}")
        break

# ✔️ Time: O(n) 
# ✔️ Space: O(1)

# ============================================
