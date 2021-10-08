class Solution:
    def maxProduct(self, nums: [int]) -> int:
        """
        当前状态有两种，一个是最大值，一个是最小值，最大值用来记录，最小值用来记录是否之后会乘一个负数变成最大值
        每次状态由三种情况产生，最大值*当前数字，最小值*当前数字，当前数字
        """
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result
#         dp = [[0, 0] for _ in range(len(nums))]
#         dp[0][0] = nums[0]
#         dp[0][1] = nums[0]
#         result = nums[0]
#         for i in range(1, len(nums)):
#             dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
#             dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
#             result = max(result, dp[i][0])

#         return result
