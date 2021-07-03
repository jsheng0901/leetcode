class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        """
        时间复杂度O(n * m)，n为正数个数，m为背包容量
        空间复杂度：O(m) m为背包容量

        假设加法的总和为x，那么减法对应的总和就是sum - x。
        所以我们要求的是 x - (sum - x) = S
        x = (S + sum) / 2
        此时问题就转化为，装满容量为x背包，有几种方法。
        :param nums:
        :param target:
        :return:
        """
        s = sum(nums)
        if target > s:
            return 0

        if (s + target) % 2 == 1:
            return 0

        big_size = int((s + target) / 2)
        dp = [0] * (big_size + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(big_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[-1]


s = Solution()
print(s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
