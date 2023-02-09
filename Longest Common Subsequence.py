def LCS(i, j, dp):
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if text1[i] == text2[j]:
        dp[i][j] = 1 + LCS(i - 1, j - 1, dp)
        return dp[i][j]
    else:
        dp[i][j] = max(LCS(i - 1, j, dp), LCS(i, j - 1, dp))
        return dp[i][j]


text1 = "abcde"
text2 = "ace"
memo = [[-1 for i in range(len(text2))] for j in range(len(text1))]
print(LCS(len(text1) - 1, len(text2) - 1, memo))