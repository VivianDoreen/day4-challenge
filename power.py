a = 3
b = 4

def power(a, b):
    if b == 0:
        return 1
    if b >= 1:
        return a * power(a, b - 1)
print(power(a, b))