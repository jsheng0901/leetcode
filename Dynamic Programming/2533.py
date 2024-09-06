class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        """
        Time O(n)
        Space O(n)
        一模一样的题目，思路同2466。
        """
        dp = [1] + [0] * maxLength
        mod = 10 ** 9 + 7

        for end in range(1, maxLength + 1):
            if end >= zeroGroup:
                dp[end] += dp[end - zeroGroup]
            if end >= oneGroup:
                dp[end] += dp[end - oneGroup]

            dp[end] %= mod

        return sum(dp[minLength: maxLength + 1]) % mod


s = Solution()
print(s.goodBinaryStrings(minLength=2, maxLength=3, oneGroup=1, zeroGroup=2))
print(s.goodBinaryStrings(minLength=4, maxLength=4, oneGroup=4, zeroGroup=3))
