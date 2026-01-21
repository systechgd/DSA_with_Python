# Example of Big O(n)

def sequence(n):
    for i in range(n):
        print(i)

# input
sequence(10)

# Drop Constance 
# doesn't matter how many n you have

def sequence(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

# input
sequence(10)

# O(2n) after drop constant result will be O(n)