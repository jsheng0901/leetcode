class Solution1:
    def maxProfit(self, prices: [int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        贪心的原则，局部最优这里是收集正利润，叠加后得到全局最优，并不需要找到波峰波谷
        收集正利润的区间，就是股票买卖的区间，而我们只需要关注最终利润，不需要记录区间
        局部最优：收集每天的正利润，全局最优：求得最大利润
        """
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)  # 负数区间直接判断为0

        return result


class Solution2:
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


s = Solution2()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))