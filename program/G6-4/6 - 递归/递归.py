from timeit import timeit


def exp(x, k):
    if k == 1:
        return x
    else:
        return exp(x, k - 1) * x


def exp2(x, k):
    result = 1
    for i in range(k):
        result *= x
    return result


def test1():
    exp(2, 5)


print(timeit(stmt=test1, number=100000))


def test2():
    exp2(2, 5)


print(timeit(stmt=test2, number=100000))
