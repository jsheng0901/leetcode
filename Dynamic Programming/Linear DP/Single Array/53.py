from typing import List


class Solution1:
    def maxSubArray(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        dp的方法，当前状态由前一个状态和当前nums取最大值算出
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = nums[0]    # 随时记录最大情况，因为最大的子序和不一定到最后一个，同时满足情况如果数组只有一个元素，则结果是第一个元素

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if dp[i] > result:
                result = dp[i]

        return result


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time O(n)
        space O(1)
        一模一样同上方法，但是因为dp的状态只由前一个状态或者当前数组元素推出，所以dp可以只需要维护一个长度就可以，及dp是一个数
        """
        dp = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            result = max(result, dp)

        return result


s = Solution1()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
