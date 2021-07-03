class Solution:
    def integerBreak(self, n: int) -> int:
        # time O(n^2), space O(n)
        # 定义dp为拆分i的最大乘积
        dp = [0] * (n + 1)

        dp[2] = 1       # 0, 1 没意义

        for i in range(3, n+1):
            for j in range(1, i - 1):
                # 定义动态规划公示最重要
                dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j))

        return dp[-1]


s = Solution()
print(s.integerBreak(n=10))
