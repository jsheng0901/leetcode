from typing import List


class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        """
        Time: O(m*n)
        Space: O(m*n)
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


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Time: O(m*n)
        Space: O(m*n)
        和第一种方法原理几乎一致。区别在于初始化第一行第一列可以放进整个loop一起，只需要初始化第一个点就行。
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # 只需要初始化起点，如果可以出发则1不能则0
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # 当初始化第一行的时候，如果不是障碍物，直接自己0+1，如果是障碍物，if直接设置为0
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    # 同理初始化行
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]


s = Solution1()
print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0], [1, 1], [0, 0]]))
