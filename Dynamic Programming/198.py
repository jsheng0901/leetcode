class Solution:
    def rob(self, nums: [int]) -> int:
        """
        动态规划，当前状态由前一天或者前两天的状态决定
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


s = Solution()
print(s.rob(nums=[1, 2, 3, 1]))
