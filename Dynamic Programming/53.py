class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        dp的方法，当前状态由前一个状态和当前nums取最大值算出
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = nums[0]    # 随时记录最大情况，因为最大的子序和不一定到最后一个

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i] > result:
                result = dp[i]

        return result


s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
