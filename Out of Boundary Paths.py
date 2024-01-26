class Solution:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        return self.recur(startRow, startColumn, maxMove, m, n, memo)

    def recur(self, i, j, maxmove, m, n, memo):
        if i >= m or j >= n or i < 0 or j < 0:
            return 1
        elif maxmove == 0:
            return 0
        elif memo[i][j][maxmove] != -1:
            return memo[i][j][maxmove]
        else:
            paths = 0
            paths += self.recur(i, j + 1, maxmove - 1, m, n, memo)
            paths += self.recur(i + 1, j, maxmove - 1, m, n, memo)
            paths += self.recur(i, j - 1, maxmove - 1, m, n, memo)
            paths += self.recur(i - 1, j, maxmove - 1, m, n, memo)
            memo[i][j][maxmove] = paths
            return paths


def test_findPaths():
    solution = Solution()
    assert solution.findPaths(2, 2, 2, 0, 0) == 6
    assert solution.findPaths(1, 3, 3, 0, 1) == 12


test_findPaths()
