class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        """
        time: O(m*n), space: O(m*n)
        动态规划的解法，此题和没有障碍的情况基本一致，区别在于遇到障碍的时候我们只需要设置为初始值0就行
        """
        # 初始位置有障碍的时候为0
        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # 构建二维数组
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        # 初始化第一行和第一列为1, 此时如果遇到了障碍物及当数值为1的时候后面的根本无法到达，全都是0
        for k in range(n):
            if obstacleGrid[0][k] != 1:
                dp[0][k] = 1
            else:
                break

        for l in range(m):
            if obstacleGrid[l][0] != 1:
                dp[l][0] = 1
            else:
                break

        # 从左向右一层一层遍历
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0], [1, 1], [0, 0]]))
