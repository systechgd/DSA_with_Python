############ List Operations / Function

# 1️⃣ Concatenate two distinct lists
lst1 = [10, 20, 30]
lst2 = [40, 50, 60]

lst3 = lst1 + lst2
print(lst3)

# 2️⃣ multiply list elements
lst = [0]

multiply_list = lst * 5
print(multiply_list)

# 3️⃣ Count element in list
count_list = [1, 2, 3, 4, 5]
print(len(count_list))

# 4️⃣ find max element in list
lst = [10, 20, 51, 45, 82, 12]
print(f"Max number: {max(lst)}")

# 5️⃣ find minimum number in list
lst = [10, 20, 51, 45, 82, 12]
print(f"Min number: {min(lst)}")

# 6️⃣ calculate sum of all element in list
count_list = [1, 2, 3, 4, 5]
print(f'Sum of elements: {sum(count_list)}')

# 7️⃣ find avarage of list element
count_list = [1, 2, 3, 4, 5]
print(f'Sum of elements: {sum(count_list)//len(count_list)}')


'''
| Symbol | Meaning                            |
| ------ | ---------------------------------- |
| **n**  | Length of the first list           |
| **m**  | Length of the second list          |
| **k**  | Total number of elements (`n + m`) |
'''

'''
| #   | Operation         | Method / Expression  | Time Complexity | Space Complexity | Explanation                        |
| --- | ----------------- | -------------------- | --------------- | ---------------- | ---------------------------------- |
| 1️⃣ | Concatenate lists | `lst1 + lst2`        | **O(n + m)**    | **O(n + m)**     | Creates a new list and copies both |
| 2️⃣ | Multiply list     | `lst * k`            | **O(n × k)**    | **O(n × k)**     | Repeats references k times         |
| 3️⃣ | Count elements    | `len(lst)`           | **O(1)**        | **O(1)**         | Length stored internally           |
| 4️⃣ | Find max          | `max(lst)`           | **O(n)**        | **O(1)**         | Scans all elements                 |
| 5️⃣ | Find min          | `min(lst)`           | **O(n)**        | **O(1)**         | Scans all elements                 |
| 6️⃣ | Sum of elements   | `sum(lst)`           | **O(n)**        | **O(1)**         | Iterates once                      |
| 7️⃣ | Average           | `sum(lst)//len(lst)` | **O(n)**        | **O(1)**         | Dominated by sum                   |
'''