class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(7, 3))
    print(Solution().uniquePaths(3, 3))
    print(Solution().uniquePaths(23, 12))
