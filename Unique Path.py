def paths(m, n, dp):
    if m == 0 or n == 0:
        return 1
    if dp[m][n] != -1:
        return dp[m][n]
    else:
        dp[m][n] = paths(m - 1, n, dp) + paths(m, n - 1, dp)
        return dp[m][n]


memo = [[-1 for i in range(7)] for j in range(3)]
print(paths(2, 6, memo))