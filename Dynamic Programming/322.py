class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        """
        完全背包的思路，这里要考虑最小额情况的初始化问题，及每个dp[j]初始化为inf除了dp[0]
        :param coins:
        :param amount:
        :return:
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):     # 遍历物品
            for j in range(coins[i], amount + 1):       # 遍历背包
                if dp[j - coins[i]] != float('inf'):    # 如果dp[j - coins[i]]是初始值则跳过，因为初始值+1还是inf
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)    # 一定要+1因为要记录此时要用到的这个coin

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]


s = Solution()
print(s.coinChange(coins=[1, 2, 5], amount=11))
