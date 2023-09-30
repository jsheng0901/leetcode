from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        dp[i][j]记录从左上角走到[i][j]需要的最小路劲和。dp[i][j]从dp[i - 1][j]和dp[i][j - 1]得到，所以我们从上到下从左到右遍历dp数组。
        初始化第一行和第一列和第一个左上角点。详细见注释。
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        # 初始化左上角为grid初始值
        dp[0][0] = grid[0][0]

        # 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 初始化第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                # 状态转移，由左和上得到
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        # 返回结果
        return dp[-1][-1]


s = Solution()
print(s.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
