################# List Comprehension

'''
📌 Key Considerations (Very Important)

1. Always creates a NEW list (not in-place)
2. Time complexity is usually O(n)
3. Space complexity is O(n) (new list)
4. Faster and cleaner than traditional loops (C-level optimization)
5. Best for simple logic
6. Avoid complex nested logic (hurts readability)
7. Supports nested loops
8. Can be used with conditions
9. Works with any iterable
10. Not memory efficient for very large data (use generators instead)
'''

# 🧩 Basic Syntax
'''
new_list = [expression for item in iterable if condition]

-> expression → what you store
-> item → loop variable
-> condition → optional filter
'''

# 1️⃣ Simple List Comprehension
lst = [1, 2, 3, 4, 5]

squares = [x*x for x in lst] 
print(f'Square of list: {squares}')

#--===================================================================

# 2️⃣ With Condition (Filtering)
lst = [10, 15, 20, 25, 30]

even = [i for i in lst if i % 2 == 0]
print(f'Even number list: {even}')

#--===================================================================

# 3️⃣ If–Else in Expression
lst = [1, 2, 3, 4]
print(f'\n{lst}')
even_with_condition = ["even" if x % 2 == 0 else "Odd" for x in lst]
print(even_with_condition,'\n')

# 📌 Note:
# if–else comes before for
# Filtering if comes after for

#--===================================================================

# 4️⃣ Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)

flat = [num for row in matrix for num in row]
print(flat)

# ✔️ Time: O(n × m)
# ✔️ Space: O(n × m)

