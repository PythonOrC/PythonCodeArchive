l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(len(l) - 1):
    print("第", i + 1, "轮")
    for j in range(len(l) - 1 - i):
        print("第", j + 1, "次对比", l[j], l[j + 1])
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
        print(l)
    print()
