# Difference terms

def print_items(a,b):
    for i in range(a):
        print(i)
    
    for i in range(b):
        print(i)

# Time complexity calculationis O(a) + O(b) = O(a+b)

def print_item(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

# Time complexity O(a) * O(b) = O(a*b)