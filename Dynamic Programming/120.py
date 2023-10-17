from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Time O(n)
        Space O(n)
        dp定义：走到第 i 行第 j 个元素的最小路径和是 dp[i][j]
        和62几乎一模一样的道理，只是在三角形的grid里面走，dp[i][j] 可以由 dp[i - 1][j] 或者 dp[i - 1][j - 1]得来，这就是状态转移公式。
        注意三角形每一行两边的特殊情况。
        """
        # 初始化一个和三角形一模一样的 dp 数组
        high = len(triangle)
        # 定义：走到第 i 行第 j 个元素的最小路径和是 dp[i][j]
        dp = [[0] * len(triangle[i]) for i in range(high)]
        # base case 定点
        dp[0][0] = triangle[0][0]

        # 进行状态转移
        for i in range(1, high):
            row = triangle[i]
            for j in range(len(row)):
                # 状态转移方程，第一种情况如果在这一层的中间
                if len(row) - 1 > j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
                # 第二种情况如果是这一层的最右边，则只有左上角
                elif j == len(row) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                # 第三种情况如果是这一层的最左边，则只有右上角
                else:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]

        # 找出落到最后一层的最小路径和
        res = float('inf')
        for k in dp[-1]:
            res = min(res, k)

        return res


s = Solution()
print(s.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
