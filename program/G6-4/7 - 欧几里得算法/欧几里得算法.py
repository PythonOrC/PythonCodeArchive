from timeit import timeit


def gcd(a, b):
    r = min(a, b) % max(a, b)
    if r == 0:
        return max(a, b)
    else:
        return gcd(min(a, b) // max(a, b), r)


def gcd2(a, b):
    c = max(a, b) - min(a, b)
    if c == 0:
        return b
    else:
        return gcd2(min(a, b), c)


print(gcd(20, 10))
print(gcd2(20, 40))
