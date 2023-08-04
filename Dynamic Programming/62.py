class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(m*n)
        Space: O(m*n)
        动态规划的解法，数论的解法极为组合问题，更偏向于数学问题，为 m + n - 2步里面有几个 m - 1步向下走的组合
        """
        # 构建二维数组
        dp = [[0 for j in range(n)] for i in range(m)]

        # 初始化第一行和第一列为1
        for k in range(n):
            dp[0][k] = 1

        for l in range(m):
            dp[l][0] = 1

        # 或者可以直接初始化所有值都为1
        # dp = [[1] * n for _ in range(m)]

        # 从左向右一层一层遍历
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Solution2:
    def dfs(self, i, j, m, n):
        if i >= m or j >= n:
            return 0
        if i == m-1 and j == n-1:
            return 1

        left = self.dfs(i+1, j, m, n)
        right = self.dfs(i, j+1, m, n)

        return left + right

    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(2^(m+n-1)-1)
        Space: O(2^(m+n-1)-1)
        机器人走过的路径可以抽象为一棵二叉树，而叶子节点就是终点，树的深度其实就是m+n-1，可以理解深搜的算法就是遍历了整个满二叉树
        深度优先模拟二叉树，找走到叶子结点的所有路径有多少种。但是超时在Leetcode上，时间复杂度太高。
        """

        return self.dfs(0, 0, m, n)


s = Solution2()
print(s.uniquePaths(m=3, n=7))
