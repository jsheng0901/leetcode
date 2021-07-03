class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        time: O(m*n), space: O(m*n)
        动态规划的解法，数论的解法极为组合问题，更偏向于数学问题，为 m + n - 2步里面有几个 m - 1步向下走的组合
        :param m:
        :param n:
        :return:
        """
        # 构建二维数组
        dp = [[0 for j in range(n)] for i in range(m)]

        # 初始化第一行和第一列为1
        for k in range(n):
            dp[0][k] = 1

        for l in range(m):
            dp[l][0] = 1

        # 从左向右一层一层遍历
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(m=3, n=7))
