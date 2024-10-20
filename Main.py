import math
def tetration(a, b):
    if b == int(b):
        result = a
        for _ in range(int(b) - 1):
            result = a ** result
        return result
    else:
        int_part = int(math.floor(b))
        frac_part = b - int_part
        result = a
        for _ in range(int_part - 1):
            result = a ** result
        result = a ** (a ** frac_part)
        result = a ** result
        return result
a = float(input("Enter the base of tetration "))
b = float(input("Enter the layer, can be decimal of tetration "))
result = tetration(a, b)
print(f"Tetration of {a}^^{b} = {result}")
