def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a, b)

a = 3
b = 5
a, b = swap(a, b)
print(a, b)