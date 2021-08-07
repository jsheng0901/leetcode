class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        """
        动态规划，找当前matrix为1的时候是正方形右下角的时候能达到的最大长度，
        最大长度由min(正上方，左侧，斜上方) + 1(自己) 构成，同时更新最大长度
        """
        res = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])

        return res ** 2
