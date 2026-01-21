# Space Complexity Notes (Easy & Interview Friendly)

## 1. What is Space Complexity?

Space Complexity tells us:

> How much **extra memory** an algorithm uses as input size grows.

We focus on **auxiliary space**, not total memory.

---

## 2. Important Rule (Very Important)

### Space Complexity =

```
Auxiliary Space (extra variables, arrays, recursion stack)
```

⚠️ **Input space is NOT counted**.

---

## 3. Why Space Complexity Matters?

* Helps write memory-efficient code
* Important for large inputs
* Interviewers often ask time + space together

---

## 4. O(1) – Constant Space

Memory used does **not change** with input size.

```java
int sum = 0;
for(int i = 0; i < n; i++) {
    sum += i;
}
```

Uses fixed variables only.

✅ **Space: O(1)**

---

## 5. O(n) – Linear Space

Extra space grows with input size.

```java
int[] arr = new int[n];
```

If `n` increases, memory increases.

✅ **Space: O(n)**

---

## 6. O(2n), O(3n) → O(n)

```java
int[] a = new int[n];
int[] b = new int[n];
```

Total space = 2n
Ignore constants.

✅ **O(n)**

---

## 7. Space Complexity and Loops

Loops **do NOT** increase space complexity.

```java
for(int i = 0; i < n; i++) {
    int x = i * 2;
}
```

Variable `x` is reused.

✅ **O(1)**

---

## 8. Space Complexity with Recursion

### Example 1: Simple Recursion

```java
void fun(int n) {
    if(n == 0) return;
    fun(n - 1);
}
```

* Recursion depth = n
* Each call uses stack space

✅ **Space: O(n)**

---

### Example 2: Binary Recursion

```java
void fun(int n) {
    if(n <= 1) return;
    fun(n - 1);
    fun(n - 1);
}
```

* Many calls, but stack depth = n

✅ **Space: O(n)**
⚠️ Time = O(2ⁿ), Space ≠ O(2ⁿ)

---

## 9. In-Place Algorithms

Algorithms that use **no extra space**.

```java
// Reverse array
for(int i = 0; i < n/2; i++) {
    swap(arr[i], arr[n-i-1]);
}
```

No extra array used.

✅ **O(1) space**

---

## 10. Common Data Structures & Space

| Data Structure     | Space Complexity |
| ------------------ | ---------------- |
| Array (n elements) | O(n)             |
| Stack              | O(n)             |
| Queue              | O(n)             |
| Linked List        | O(n)             |
| HashMap            | O(n)             |
| Variables only     | O(1)             |

---

## 11. Time vs Space Example

```java
for(int i = 0; i < n; i++) {
    print(i);
}
```

* Time: O(n)
* Space: O(1)

---

## 12. Common Interview Mistakes

❌ Loop runs n times → space is O(n)
✅ Loop runs n times but uses same memory → space is O(1)

---

## 13. Best Interview Line 🧠

> "We consider only auxiliary space and ignore input space."

---

## 14. Quick Memory Tricks

* Only variables → O(1)
* Array / list / map → O(n)
* Recursion → O(depth)
* Loop ≠ extra space

---

## ✅ Final Summary

* Space ≠ Time
* Count **extra memory**
* Recursion stack matters
* In-place is best

---

Happy DSA Preparation 🚀
