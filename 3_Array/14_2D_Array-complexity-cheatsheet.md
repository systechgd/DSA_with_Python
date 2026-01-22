# 🧠 NumPy 2D Array CRUD Cheat Sheet (with Methods & Complexity)

> **Assume array size = n × m**
> NumPy arrays are **fixed-size & contiguous in memory**

---

### 📐 Notation Used in This Cheat Sheet

| Symbol | Meaning                                                                                        |
| ------ | ---------------------------------------------------------------------------------------------- |
| **n**  | Number of **rows** in the 2D NumPy array                                                       |
| **m**  | Number of **columns** in the 2D NumPy array                                                    |
| **k**  | Number of **selected / affected rows or elements** (e.g., fancy indexing, boolean mask result) |

---

| CRUD  | Operation          | Method / Syntax               | Time Complexity | Space Complexity | Key Notes             |
| ----- | ------------------ | ----------------------------- | --------------- | ---------------- | --------------------- |
| **C** | Create empty       | `np.empty((n,m))`             | **O(1)**        | **O(nm)**        | Memory allocated only |
| **C** | Create zeros       | `np.zeros((n,m))`             | **O(nm)**       | **O(nm)**        | Initializes all       |
| **C** | Create ones        | `np.ones((n,m))`              | **O(nm)**       | **O(nm)**        | Initializes all       |
| **C** | From list          | `np.array(list2d)`            | **O(nm)**       | **O(nm)**        | Copies data           |
| **C** | Copy array         | `arr.copy()`                  | **O(nm)**       | **O(nm)**        | Deep copy             |
| **R** | Read element       | `arr[i, j]`                   | **O(1)**        | **O(1)**         | Direct index          |
| **R** | Read row           | `arr[i]`                      | **O(1)**        | **O(1)**         | View (no copy)        |
| **R** | Read column        | `arr[:, j]`                   | **O(1)**        | **O(1)**         | View using stride     |
| **R** | Slice              | `arr[1:4, :]`                 | **O(1)**        | **O(1)**         | View                  |
| **R** | Fancy index        | `arr[[0,2]]`                  | **O(km)**       | **O(km)**        | Copy created          |
| **U** | Update element     | `arr[i, j] = x`               | **O(1)**        | **O(1)**         | In-place              |
| **U** | Update row         | `arr[i] = row`                | **O(m)**        | **O(1)**         | Overwrites row        |
| **U** | Update column      | `arr[:, j] = col`             | **O(n)**        | **O(1)**         | Strided write         |
| **U** | Broadcast update   | `arr += 1`                    | **O(nm)**       | **O(1)**         | In-place              |
| **U** | Conditional update | `arr[arr>5]=0`                | **O(nm)**       | **O(k)**         | Mask created          |
| **D** | Delete row         | `np.delete(arr, i, axis=0)`   | **O(nm)**       | **O(nm)**        | New array             |
| **D** | Delete column      | `np.delete(arr, j, axis=1)`   | **O(nm)**       | **O(nm)**        | Copy                  |
| **D** | Delete many        | `np.delete(arr,[i,j],axis=0)` | **O(nm)**       | **O(nm)**        | Copy                  |
| **D** | Filter rows        | `arr[arr[:,0]>5]`             | **O(nm)**       | **O(km)**        | Boolean mask          |
| **I** | Insert row         | `np.insert(arr,i,row,axis=0)` | **O(nm)**       | **O(nm)**        | Copy + shift          |
| **I** | Insert column      | `np.insert(arr,j,col,axis=1)` | **O(nm)**       | **O(nm)**        | Copy                  |
| **I** | Append row         | `np.append(arr,row,axis=0)`   | **O(nm)**       | **O(nm)**        | New array             |
| **I** | Concatenate        | `np.vstack()` / `np.hstack()` | **O(nm)**       | **O(nm)**        | Copies all            |

### 📌 One-Line Exam Rule (Remember This)

> **Access & Update → O(1)**
> **Insert / Delete → O(nm) time & space**
> **Reason: NumPy arrays are fixed-size**

### ⚠️ Common Confusions (Quick Fix)

- **Slicing ≠ Copy** → slicing gives **view**
- **Fancy indexing = Copy**
- **Delete is never in-place**
- **np.append ≠ list append**
