class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        dp[i][0] 表示第i天持有股票所得现金。
        dp[i][1] 表示第i天不持有股票所得最多现金
        :param prices:
        :return:
        """
        if len(prices) == 0:
            return 0

        dp = [[0, 0] for i in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

        return dp[-1][1]


s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
