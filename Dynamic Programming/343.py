class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Time O(n^2)
        Space O(n)
        定义dp[i]为拆分i的最大乘积
        动态规划公示意思是i最大的拆分为: 从1遍历j，然后有两种渠道得到dp[i]，一个是j * (i - j) 直接相乘。一个是j * dp[i - j]。
        j * (i - j) 是单纯的把整数拆分为两个数相乘，而j * dp[i - j]是拆分成两个以及两个以上的个数相乘。
        """
        dp = [0] * (n + 1)

        dp[2] = 1       # 0, 1 没意义

        for i in range(3, n+1):
            for j in range(1, i - 1):
                # 定义动态规划公示最重要
                dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j))

        return dp[-1]


s = Solution()
print(s.integerBreak(n=10))
