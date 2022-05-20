def frog(n):

    if n == 1 or n == 0:
        return 1
    else:
        return frog(n - 2) + frog(n - 1)


print(frog(7))
