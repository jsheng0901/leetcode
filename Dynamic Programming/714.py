class Solution:
    def maxProfit(self, prices: [int], fee: int) -> int:
        """
        time O(n), space O(1), 此题更适合动态规划的思路，贪心的思路只是锻炼
        dp[i][0] 第i天持有股票所省最多现金
        dp[i][1] 第i天不持有股票所省最多现金
        """
        if len(prices) == 0:
            return 0

        dp = [[0, 0] for i in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)

        return dp[-1][-1]


s = Solution()
print(s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
