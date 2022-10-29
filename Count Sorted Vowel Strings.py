def countVowelStrings(n):
    dp = [0] + [1] * 5
    for i in range(1, n + 1):
        for k in range(1, 6):
            dp[k] += dp[k - 1]
    return dp[5]

print(countVowelStrings(33))