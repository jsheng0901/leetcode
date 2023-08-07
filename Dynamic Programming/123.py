class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        一天一共就有五个状态, 没有操作, 第一次买入, 第一次卖出, 第二次买入, 第二次卖出
        dp[i][j]中 i表示第i天，j为 [0 - 4] 五个状态，dp[i][j]表示第i天状态j所剩最大现金。
        """
        dp = [[0, 0, 0, 0, 0] for i in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])      # 没有操作或者买入股票
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])      # 没有操作或者卖出股票
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return dp[-1][-1]


s = Solution()
print(s.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
