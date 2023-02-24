Coins = [1, 2, 5]
Amount = 11


def coinChange(coins, amount):
    coins.sort()
    DP = [float("inf")] * (amount + 1)
    DP[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                DP[i] = min(DP[i], DP[i - coin] + 1)
    else:
        return DP


print(coinChange(Coins, Amount))
