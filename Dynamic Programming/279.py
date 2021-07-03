class Solution:
    def numSquares(self, n: int) -> int:
        """
        转化成完全背包: 完全平方数就是物品（可以无限件使用），凑个正整数n就是背包，问凑满这个背包最少有多少物品？
        :param n:
        :return:
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n+1):  # 遍历背包
            j = 1
            while j * j <= i:   # 遍历物品
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        # 方案2，先遍历物品在遍历背包
        # i = 1
        # while i * i <= n:       # 物品
        #     for j in range(i * i, n + 1):       # 背包
        #         dp[j] = min(dp[j], dp[j - i * i] + 1)
        #
        #     i += 1

        return dp[-1]


s = Solution()
print(s.numSquares(n=12))
