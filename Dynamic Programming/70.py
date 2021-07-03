class Solution:
    def climbStairs(self, n: int) -> int:
        """
        time O(n), space O(n)
        动态规划思路，i的方法取决于前两步方法的和，其实就是斐波那契数列，只是没有0的状态
        :param n:
        :return:
        """
        if n <= 1:
            return n

        dp = [0] * (n + 1)  # 有0

        # 初始化
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    def climbStairs2(self, n: int) -> int:
        """
        time O(n), space O(1), save space for only store three value
        :param n:
        :return:
        """
        if n <= 1:
            return n

        # 初始化
        dp = [0, 1, 2]

        for i in range(3, n + 1):
            s = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = s

        return dp[-1]


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        完全背包思路，爬多少步是物品，到底几层是背包的weight，dp[i]表示背包重量是i的时候有几种方法放满
        :param n:
        :return:
        """
        if n <= 1:
            return n

        dp = [0] * (n + 1)  # 有0

        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, 3):
                if i - j >= 0:
                    dp[i] += dp[i - j]

        return dp[n]


s = Solution()
print(s.climbStairs2(5))