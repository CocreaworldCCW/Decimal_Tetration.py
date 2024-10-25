import math

def super_logarithm(x, base):
    if x < 1:
        raise ValueError("x must be greater than or equal to 1.")
    if base <= 1:
        raise ValueError("base must be greater than 1.")
    count = 0
    while x >= base:
        x = math.log(x, base)
        count += 1
    if x > 1:
        count += math.log(x, base)

    return count
