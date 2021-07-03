class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        """
        dp的方法，当前状态由前一个状态和当前nums取最大值算出
        :param nums:
        :return:
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i] > result:
                result = dp[i]

        return result


s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
