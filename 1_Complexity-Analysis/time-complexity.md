# Time Complexity Notes (Easy & Interview Friendly)

## 1. What is Time Complexity?

Time Complexity tells us:

> How the **running time of an algorithm grows** when input size grows.

We do **not** measure actual time (seconds).
We measure **number of operations**.

---

## 2. Why Time Complexity is Important?

* Helps compare algorithms
* Tells if code will work for large input
* Interviewers always ask it

---

## 3. Big-O Notation

We represent time complexity using **Big-O**.

Example:

* O(1)
* O(n)
* O(n²)

Big-O shows the **worst-case performance**.

---

## 4. Important Rules (Must Remember)

### Rule 1: Ignore Constants

* O(2n) → O(n)
* O(5) → O(1)

### Rule 2: Ignore Smaller Terms

* O(n² + n) → O(n²)
* O(n + log n) → O(n)

👉 **The fastest growing term wins**

---

## 5. Common Time Complexities

### O(1) – Constant Time

Time does not depend on input size.

```java
int x = arr[0];
```

Examples:

* Access array element
* Assign a variable

---

### O(n) – Linear Time

Time grows directly with input size.

```java
for(int i = 0; i < n; i++) {
    print(i);
}
```

* 1 loop → O(n)

---

### O(2n), O(3n) → O(n)

```java
for(int i = 0; i < n; i++) {}
for(int i = 0; i < n; i++) {}
```

Steps = 2n
Ignore constants → **O(n)**

---

### O(n²) – Quadratic Time

Nested loops.

```java
for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        print(i, j);
    }
}
```

* 2 nested loops → O(n²)

---

### O(n³)

Three nested loops.

```java
for(i)
  for(j)
    for(k)
```

Very slow, avoid if possible.

---

### O(log n) – Logarithmic Time

Input size is **divided** each step.

```java
while(n > 1) {
    n = n / 2;
}
```

Examples:

* Binary Search
* Divide and conquer

---

### O(n log n)

Combination of loop + log.

Examples:

* Merge Sort
* Quick Sort (average case)

---

### O(2ⁿ) – Exponential Time

Very slow.

Example:

* Recursive Fibonacci

---

## 6. Loop Based Time Complexity

| Code Pattern         | Time Complexity |
| -------------------- | --------------- |
| No loop              | O(1)            |
| One loop             | O(n)            |
| Two nested loops     | O(n²)           |
| Three nested loops   | O(n³)           |
| Loop with division   | O(log n)        |
| Loop + binary search | O(n log n)      |

---

## 7. Examples

### Example 1

```java
for(int i = 0; i < n; i++) {
    print(i);
}
```

**Time:** O(n)

---

### Example 2

```java
for(int i = 0; i < n; i++) {
    for(int j = i; j < n; j++) {
        print(i, j);
    }
}
```

**Time:** O(n²)

---

### Example 3

```java
for(int i = 0; i < n; i++) {
    binarySearch(arr);
}
```

**Time:** O(n log n)

---

## 8. Best to Worst Time Complexity Order

```
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
```

---

## 9. Interview Tips

* Always mention **worst case**
* Say:

  > "We ignore constants and smaller terms and take the dominant term"
* Practice identifying loops quickly

---

## 10. Quick Memory Trick

* Count loops
* Check nesting
* Check division by 2
* Drop constants

---

## ✅ Final Note

If you can identify loops and recursion depth,
you can calculate time complexity in **under 30 seconds**.

---

Happy Coding 🚀
