class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        """
        dp: time O(n), space O(n)
        greedy: time O(n), space O(1)
        此题和300很像，区别在于连续，所有每次都要判断大小，并记录最长连续子序列
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return len(nums)

        dp = [1] * len(nums)
        result = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1  # 这里直接+1，因为前一个小于后一个则直接是连续递增子序列
                if dp[i] > result:  # 非常重要，一定要赋值给最长子序列长度，不然不知道到数组哪里是最长连续子序列
                    result = dp[i]
        return result


s = Solution()
print(s.findLengthOfLCIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
