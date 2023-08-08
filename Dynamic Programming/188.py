class Solution:
    def maxProfit(self, k: int, prices: [int]) -> int:
        """
        Time O(n * k)   n为price的长度
        Space O(n * k)
        一天一共就有2k + 1个状态, 没有操作, 第一次买入, 第一次卖出, 第二次买入, 第二次卖出, ...
        dp[i][j]中 i表示第i天，j为 [0 - 2k+1] 五个状态，dp[i][j]表示第i天状态j所剩最大现金。
        每天的情况比较多且复杂, 并且这里和123的区别在于操作次数是dynamic的
        """
        dp = [[0] * (2*k + 1) for i in range(len(prices))]

        for i in range(1, 2*k, 2):
            dp[0][i] = -prices[0]

        # 遍历每一天的股票
        for i in range(1, len(prices)):
            # 遍历每天的每一种状态
            for j in range(0, 2*k - 1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j]-prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1]+prices[i])

            # 另一种写法
            # for j in range(1, 2 * k + 1, 2):
            #     dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
            #     dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] + prices[i])

        return dp[-1][-1]


s = Solution()
print(s.maxProfit(k=2, prices=[3, 3, 5, 0, 0, 3, 1, 4]))
