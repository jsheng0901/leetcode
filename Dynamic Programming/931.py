from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Time O(n * n)
        Space O(n * n)
        dp数组定义：dp[i][j]是从第一行走到[i][j]的最小路径和。
        根据题目含义，当前位置dp[i][j]只能从三个方向得来，及dp[i - 1][j]，dp[i - 1][j - 1]，dp[i - 1][j + 1]。
        也就是每次取这三个的最小值即可。注意考虑matrix两边可能越界的情况，计算j的时候。
        """
        n = len(matrix)

        dp = [[0] * n for _ in range(n)]

        # 初始化第一行，因为每一行是由上一行推导出来，第一行显然等于matrix自己
        for j in range(n):
            dp[0][j] = matrix[0][j]

        # 从上到下，从左到右遍历
        for i in range(1, n):
            for j in range(n):
                # 第一列，则没有[j-1]的情况
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                # 最后一列，则没有[j+1]的情况
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                # 三种方向遍历
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + matrix[i][j]

        # 最后我们要遍历一遍最后一行找到最小值，因为不知道到那一列最后一行是最小值。
        result = float('inf')
        for j in range(n):
            result = min(result, dp[n - 1][j])

        return result


class Solution2:
    def dp(self, matrix, i, j, memo, m, n):
        # 返回值保证一定是大于所有path总和的最大值就行，也就是后面去min一定会去掉
        if i < 0 or i >= m or j < 0 or j >= n:
            return 99999

        if i == 0:
            return matrix[0][j]

        if memo[i][j] != 666:
            return memo[i][j]

        # 三个方向取最小值
        left = self.dp(matrix, i - 1, j - 1, memo, m, n)
        right = self.dp(matrix, i - 1, j + 1, memo, m, n)
        above = self.dp(matrix, i - 1, j, memo, m, n)
        sub = matrix[i][j] + min(left, right, above)

        memo[i][j] = sub

        return memo[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        一模一样的思路，只是换成从下往上写的方式。
        """
        m, n = len(matrix), len(matrix[0])
        # 初始值保证不会取到就行，参考题目给的constrict
        memo = [[666] * n for _ in range(m)]

        res = float('inf')
        for j in range(n):
            res = min(res, self.dp(matrix, n - 1, j, memo, m, n))

        return res


s = Solution()
print(s.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
