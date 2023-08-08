class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        总共四种状态
        状态一：买入股票状态（今天买入股票，或者是之前就买入了股票然后没有操作）
        卖出股票状态，这里就有两种卖出股票状态
                    状态二：两天前就卖出了股票，度过了冷冻期，一直没操作，今天保持卖出股票状态
                    状态三：今天卖出了股票
        状态四：今天为冷冻期状态，但冷冻期状态不可持续，只有一天！
        """
        if len(prices) == 0:
            return 0

        dp = [[0, 0, 0, 0] for i in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            # 状态一的情况:
            # 操作一：前一天就是持有股票状态（状态一），dp[i][0] = dp[i - 1][0]
            # 操作二：今天买入了，有两种情况:
            #           前一天是冷冻期（状态四），dp[i - 1][3] - prices[i]
            #           前一天是保持卖出股票的状态（状态二），dp[i - 1][1] - prices[i]
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]

        return max(dp[-1][1], dp[-1][2], dp[-1][3])


s = Solution()
print(s.maxProfit(prices=[1, 2, 3, 0, 2]))
