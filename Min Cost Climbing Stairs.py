cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1, 0]
for i in range(len(cost) - 3, -1, -1):
    cost[i] += min(cost[i + 1], cost[i + 2])
print(min(cost[0], cost[1]))
