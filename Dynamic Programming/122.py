class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        和121一样，只是计算持有股票的时候要考虑之前的盈利情况
        """
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])      # 考虑之前的盈利情况dp[i-1][1]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])

        return dp[-1][1]


s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))