prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
i, j = 0, 1
maX = -1 * float("inf")
if len(prices) > 2:
    while i < len(prices) - 1:
        if i == j:
            j += 1
        if j > len(prices) - 1:
            i += 1
            j = i + 1
        elif prices[i] >= prices[j]:
            i += 1
        else:
            maX = max(prices[j] - prices[i], maX)
            j += 1
    if maX >= 0:
        print(maX)
    else:
        print(0)
elif len(prices) == 2:
    if prices[0] < prices[1]:
        print(prices[1] - prices[0])
    else:
        print(0)
else:
    print(0)
