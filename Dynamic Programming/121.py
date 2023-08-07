class Solution:
    def maxProfit1(self, prices: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        dp[i][0] 表示第i天持有股票所得现金。
        dp[i][1] 表示第i天不持有股票所得最多现金
        """
        if len(prices) == 0:
            return 0

        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])

        return dp[-1][1]

    def maxProfit2(self, prices: [int]) -> int:
        """
        Time O(n)
        Space O(1)
        贪心算法，永远找最小的买股票时间，同时更新最大间隔差
        """
        result = 0
        min_left = float('inf')

        for i in range(len(prices)):
            min_left = min(min_left, prices[i])     # 最小的买股票时间
            result = max(result, prices[i] - min_left)      # 更新最大间隔差

        return result


s = Solution()
print(s.maxProfit1(prices=[7, 1, 5, 3, 6, 4]))
