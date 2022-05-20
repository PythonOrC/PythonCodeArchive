import random
arr = []
while len(arr) < 28:
    A1 = random.randint(0,2)
    B1 = 2-A1

    B2 = random.randint(0,2)
    C2 = 2-B2

    A3 = random.randint(0,2)
    C3 = 2-A3

    ls = [A1+A3,B2+B1,C2+C3]
    if ls not in arr:
        arr.append(ls)

    print(len(arr))


