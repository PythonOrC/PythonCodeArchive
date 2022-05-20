for i in range(100, 1000):
    if (i // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 10) ** 3 == i:
        print(i)

for d3 in range(1, 10):
    for d2 in range(10):
        for d1 in range(10):
            if d3 ** 3 + d2 ** 3 + d1 ** 3 == d3 * 100 + d2 * 10 + d1:
                print(d3 * 100 + d2 * 10 + d1)


num = 4567
print(num // 1000, num // 100 % 10, num // 10 % 10, num % 10)
