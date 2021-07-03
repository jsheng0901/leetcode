class Solution:
    def fib(self, n: int) -> int:
        """
        time O(n), space O(n)
        :param n:
        :return:
        """
        if n <= 1:
            return n

        dp = [0] * (n + 1)  # 有0

        # 初始化
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    def fib2(self, n: int) -> int:
        """
        time O(n), space O(1), save space for only store two value
        :param n:
        :return:
        """
        if n <= 1:
            return n

        # 初始化
        dp = [0, 1]

        for i in range(2, n + 1):
            s = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = s

        return dp[-1]

    def fib3(self, n: int) -> int:
        """
        time O(2^n), space O(n)
        递归的方式，树状图
        :param n:
        :return:
        """
        if n <= 1:
            return n

        return self.fib3(n-1) + self.fib3(n-2)


s = Solution()
print(s.fib3(10))
