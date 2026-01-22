# 🧠 Python Array - Foundation for DSA

This folder focuses on **array fundamentals** as part of **Data Structures & Algorithms (DSA)** practice.
The goal is to understand **how arrays work, how they are accessed, and how they are stored in memory**.

---

## 🔹 What is an Array?

An **array** is a data structure that:

- Stores elements in a **contiguous block of memory**
- Allows **direct access** using an index
- Stores **homogeneous data** (same data type)

⚠️ Python does not have a **true built-in array** like C/C++.
Instead, we use:

- **Python Lists** (dynamic, flexible)
- **NumPy Arrays** (fixed type, contiguous memory, closer to DSA arrays)

---

## 🔹 Key Characteristics of Arrays (DSA Perspective)

- Elements are stored in **contiguous memory locations**
- Each element has a **unique index**
- Indexing starts from **0**
- Allows **O(1) time complexity** for access
- Efficient for traversal and mathematical operations

---

## 🔹 Types of Arrays

---

## 1️⃣ One-Dimensional Array (1D)

- Single row, multiple elements
- Accessed using **one index**

### Example

```python
arr = [10, 20, 30, 40]
print(arr[2])   # Output: 30
```

### Access Format

```
arr[index]
```

### Memory Representation (Conceptual)

```
Index:   0     1     2     3
        ┌───┬───┬───┬───┐
Value:  │10 │20 │30 │40 │
        └───┴───┴───┴───┘
Memory: 1000  1004  1008  1012   (example addresses)
```

✔ Each element is stored **next to each other in memory**

---

## 2️⃣ Two-Dimensional Array (2D)

- Multiple rows and columns
- Represented as a **matrix**
- Accessed using **row index and column index**

### Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # Output: 6
```

### Access Format

```
arr[row_index][column_index]
```

### Visual Representation

```
Columns →
     0   1   2
Rows
0   [ 1   2   3 ]
1   [ 4   5   6 ]
2   [ 7   8   9 ]
```

### Memory Representation (Row-wise)

```
Row 0 →  [1][2][3]  → contiguous
Row 1 →  [4][5][6]  → contiguous
Row 2 →  [7][8][9]  → contiguous
```

✔ Each **row is stored contiguously**
✔ Rows are accessed via **row references**

---

## 3️⃣ Three-Dimensional Array (3D)

- Multiple layers of 2D arrays
- Used in:
  - 3D matrices
  - Image processing
  - Time-series data

- Accessed using **layer, row, and column**

### Example (2 Layers × 2 Rows × 2 Columns)

```python
arr = [
    [  # Layer 0
        [1, 2],
        [3, 4]
    ],
    [  # Layer 1
        [5, 6],
        [7, 8]
    ]
]

print(arr[1][0][1])  # Output: 6
```

### Access Format

```
arr[layer][row][column]
```

### Visual Representation

```
Layer 0        Layer 1
[ [1, 2],      [ [5, 6],
  [3, 4] ]       [7, 8] ]
```

---

## 🔹 How Arrays Are Stored in Memory (Important for DSA)

### Contiguous Memory Concept

```
Base Address = 1000

arr[0] → 1000
arr[1] → 1004
arr[2] → 1008
arr[3] → 1012
```

📌 Address Formula (Conceptual):

```
Address of arr[i] = Base Address + (i × size_of_element)
```

This is why:

- Access is **O(1)**
- Arrays are faster than linked structures for indexing

---

## 🔹 Python List vs NumPy Array (DSA View)

| Feature     | Python List    | NumPy Array |
| ----------- | -------------- | ----------- |
| Data Type   | Mixed          | Same type   |
| Memory      | Non-contiguous | Contiguous  |
| Performance | Slower         | Faster      |
| DSA Usage   | Conceptual     | Practical   |

---

## 🔹 Why Arrays Are Important in DSA

- Foundation for:
  - Strings
  - Matrices
  - Heaps
  - Hashing

- Used in:
  - Searching
  - Sorting
  - Sliding Window
  - Two Pointer techniques

---

## 📌 Summary

- Arrays store data in **contiguous memory**
- Indexing allows **constant-time access**
- 1D, 2D, and 3D arrays are core building blocks
- Understanding memory layout is **critical for DSA problem-solving**

---

## 📌 recommendation (important)

| Purpose                        | What to Use |
| ------------------------------ | ----------- |
| Learn DSA                      | ✅ `list`   |
| Coding interviews              | ✅ `list`   |
| Competitive programming        | ✅ `list`   |
| Memory-critical low-level work | `array`     |
| Data science / ML              | NumPy       |
