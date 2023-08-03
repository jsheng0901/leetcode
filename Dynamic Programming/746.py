class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        初始化前两步，第三步取决去前两步最小的数据加当前这步
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[-1], dp[-2])

    def minCostClimbingStairs2(self, cost: [int]) -> int:
        """
        Time O(n)
        Space O(1), save space for only store two value
        初始化前两步，第三步取决去前两步最小的数据加当前这步
        """

        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            dpi = min(dp[0], dp[1]) + cost[i]
            dp[0] = dp[1]
            dp[1] = dpi

        return min(dp)

    def minCostClimbingStairs3(self, cost: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        另一种写法，当到达最后一步的时候判断一下，改变动态规划公示
        """
        if len(cost) <= 2:
            return min(cost)

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            if i != len(cost) - 1:      # 判断是否是最后一步
                dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
            else:
                dp[i] = min(dp[i - 1], dp[i - 2] + cost[i])

        return dp[-1]


s = Solution()
print(s.minCostClimbingStairs2(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
