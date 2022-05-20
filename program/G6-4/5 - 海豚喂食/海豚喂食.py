def feed(dolphin, food):
    cnt = 0
    i = 0
    j = 0

    dolphin.sort()
    food.sort()

    while i < len(dolphin) and j < len(food):
        if food[j] >= dolphin[i]:
            i += 1
            cnt += 1
        j += 1
    return cnt


dolphin = [7, 15, 3, 10, 5]
food = [10, 1, 2, 8, 4]

print(feed(dolphin, food))
