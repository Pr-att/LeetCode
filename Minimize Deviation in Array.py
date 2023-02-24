import heapq


def minimumDeviation(nums):
    array = [-n if not n % 2 else -2 * n for n in set(nums)]
    heapq.heapify(array)
    Min = -max(array)
    res = float("inf")

    while not array[0] % 2:
        Max = -heapq.heappop(array)
        heapq.heappush(array, -Max // 2)
        res = min(res, Max - Min)
        Min = min(Min, Max // 2)

    return min(-array[0] - Min, res)


# print(minimumDeviation([1, 2, 3, 4]))
print(minimumDeviation([4, 1, 5, 20, 3]))
print(minimumDeviation([1, 2, 3, 4]))
print(minimumDeviation([3, 5]))
print(minimumDeviation([6, 12]))
