prices = [7, 1, 5, 3, 6, 4]
length = len(prices)
array = [-1] * (2 * length)
array[0] = 0
array[1] = -1 * prices[0]
for j in range(2, (length * 2), 2):
    array[j] = max(array[j - 2], prices[j // 2] + array[j - 1])
    array[j + 1] = max(array[j - 2] - prices[j // 2], array[j - 1])
print(max(array))