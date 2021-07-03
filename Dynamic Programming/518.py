class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        """
        完全背包问题，考虑组合问题这不需要考虑顺序，所以不能重复

        如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        如果求排列数就是外层for遍历背包，内层for循环遍历物品
        :param amount:
        :param coins:
        :return:
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):     # 遍历物品
            for j in range(coins[i], amount + 1):       # 遍历背包，这种遍历方式不会重复计算{1, 5}和{5, 1}这同一种组合两次
                dp[j] += dp[j - coins[i]]

        return dp[-1]


s = Solution()
print(s.change(amount=5, coins=[1, 2, 5]))
