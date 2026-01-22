# 📌 1-D Array CRUD Operations – Time & Space Complexity Cheatsheet

## Assumptions

- n = number of elements
- Index-based access

---

## 📊 CRUD Operations Complexity Table

| Operation             | Method / Example | Time Complexity | Space Complexity | Notes                 |
| --------------------- | ---------------- | --------------- | ---------------- | --------------------- |
| Create                | arr = [1,2,3]    | O(n)            | O(n)             | Allocate & initialize |
| Read (Access)         | arr[i]           | O(1)            | O(1)             | Direct index access   |
| Read (Search)         | x in arr         | O(n)            | O(1)             | Linear search         |
| Update (by index)     | arr[i] = x       | O(1)            | O(1)             | Overwrite             |
| Update (by value)     | find + update    | O(n)            | O(1)             | Search required       |
| Delete (by index)     | del arr[i]       | O(n)            | O(1)             | Shifting elements     |
| Delete (by value)     | arr.remove(x)    | O(n)            | O(1)             | Search + shift        |
| Insert (at end)       | arr.append(x)    | O(1) amortized  | O(1)             | Occasional resize     |
| Insert (at index)     | arr.insert(i, x) | O(n)            | O(1)             | Shifting              |
| Insert (at beginning) | arr.insert(0, x) | O(n)            | O(1)             | Worst shifting        |
| Traversal             | for x in arr     | O(n)            | O(1)             | Visit all             |

---

## ⚠️ Commonly Confusing Methods

### 1️⃣ append() vs insert()

| Method       | Time           | Explanation     |
| ------------ | -------------- | --------------- |
| append(x)    | O(1) amortized | Adds at end     |
| insert(i, x) | O(n)           | Shifts elements |

---

### 2️⃣ remove() vs pop()

| Method    | Time | Reason         |
| --------- | ---- | -------------- |
| remove(x) | O(n) | Search + shift |
| pop()     | O(1) | Removes last   |
| pop(i)    | O(n) | Shifting       |

---

### 3️⃣ Membership vs Index Access

| Operation | Time |
| --------- | ---- |
| arr[i]    | O(1) |
| x in arr  | O(n) |

---

### 4️⃣ Slicing (Very Common Confusion)

arr[1:5]

| Aspect | Complexity |
| ------ | ---------- |
| Time   | O(k)       |
| Space  | O(k)       |

Note: Creates a new array

---

### 5️⃣ Sorting

| Method      | Time       | Space  |
| ----------- | ---------- | ------ |
| arr.sort()  | O(n log n) | O(1)\* |
| sorted(arr) | O(n log n) | O(n)   |

- Timsort uses hidden auxiliary memory

---

### 6️⃣ Reversing

| Method        | Time | Space |
| ------------- | ---- | ----- |
| arr.reverse() | O(n) | O(1)  |
| arr[::-1]     | O(n) | O(n)  |

---

## 🧠 Static Array (Theory / Interviews)

| Operation | Time |
| --------- | ---- |
| Insert    | O(n) |
| Delete    | O(n) |

---

## ✅ Quick Summary

- Access → O(1)
- Search → O(n)
- Insert/Delete (middle/start) → O(n)
- Append → O(1) amortized
- Slicing creates a new array
- remove() ≠ pop()
