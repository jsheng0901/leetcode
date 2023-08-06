class Solution:
    def rob_range(self, nums: [int]) -> int:
        """
        动态规划，当前状态由前一天或者前两天的状态决定，这部分如198一模一样
        """
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    def rob(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        两种状态，第一种不考虑最后一个，第二种不考虑第一个
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        range1_result = self.rob_range(nums[: -1])
        range2_result = self.rob_range(nums[1: ])

        return max(range2_result, range1_result)


s = Solution()
print(s.rob(nums=[1, 2, 3, 1]))
