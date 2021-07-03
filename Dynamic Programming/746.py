class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        """
        time O(n), space O(n)
        初始化前两步，第三步取决去前两步最小的数据加当前这步
        :param cost:
        :return:
        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[-1], dp[-2])

    def minCostClimbingStairs2(self, cost: [int]) -> int:
        """
        time O(n), space O(1), save space for only store two value
        初始化前两步，第三步取决去前两步最小的数据加当前这步
        :param cost:
        :return:
        """

        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            dpi = min(dp[0], dp[1]) + cost[i]
            dp[0] = dp[1]
            dp[1] = dpi

        return min(dp)


s = Solution()
print(s.minCostClimbingStairs2(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
