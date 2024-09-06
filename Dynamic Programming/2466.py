class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        Time O(n)
        Space O(n)
        dp[i] -> 长度为i的string，有多少个合理的string。
        这里考虑两种情况，
        case 1：如果i是0结尾，dp[end] += dp[end - zero -> 0的个数]    ex: dp[5] = dp[4] + "0"
        case 2：如果i是1结尾，dp[end] += dp[end - one -> 1的个数]     ex: dp[5] = dp[3] + "11"
        """
        # dp[0] = 1 初始化，因为空的string是唯一一个合理的string
        dp = [1] + [0] * high
        mod = 10 ** 9 + 7

        for end in range(1, high + 1):
            # case 1
            # 判断一下结尾的长度是否大于题目要求的0个数
            if end >= zero:
                dp[end] += dp[end - zero]
            # case 2
            # 判断一下结尾的长度是否大于题目要求的1个数
            if end >= one:
                dp[end] += dp[end - one]

            dp[end] %= mod

        # sum 起来所有符合题意的长度的结果
        return sum(dp[low: high + 1]) % mod


s = Solution()
print(s.countGoodStrings(low=3, high=3, zero=1, one=1))
