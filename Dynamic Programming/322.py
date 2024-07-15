from typing import Union, List


class Solution:
    def coinChange(self, coins: [int], amount: int) -> Union[int, float]:
        """
        Time O(n * m)  n --> number of coins   m --> amount
        Space O(m)
        完全背包的思路，这里要考虑最小额情况的初始化问题，及每个dp[j]初始化为inf除了dp[0]
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


class Solution2:
    def __init__(self):
        self.memo = None

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        # 查备忘录，防止重复计算
        if self.memo[amount] != -666:
            return self.memo[amount]

        res = float('inf')
        for coin in coins:
            # 计算子问题的结果
            sub_problem = self.dp(coins, amount - coin)

            # 子问题无解则跳过
            if sub_problem == -1:
                continue
            # 在子问题中选择最优解，然后加一
            res = min(res, sub_problem + 1)

        # 把计算结果存入备忘录
        self.memo[amount] = -1 if res == float('inf') else res

        return self.memo[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-666] * (amount + 1)
        # dp 数组全都初始化为特殊值
        return self.dp(coins, amount)


s = Solution()
print(s.coinChange(coins=[1, 2, 5], amount=11))
