# Big O(logN)
# technique devide and conquer

# def log_example(n):
#     count = 0
#     while n > 1:
#         n = n // 2
#         count += 1
#     return count

# operations = log_example(16)

# print(f"Number of opeartion/steps required : {operations}")


# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

target_index = binary_search(list(range(1,9)), 6)
print(target_index)