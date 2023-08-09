class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        """
        Time O(n^2)
        Space O(n)
        动态规划公示：位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
        """
        if len(nums) <= 1:
            return len(nums)

        dp = [1] * len(nums)
        result = 0

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 注意这里不是要dp[i] 与 dp[j] + 1进行比较，而是我们要取dp[j] + 1的最b大值。
            if dp[i] > result:   # 非常重要，一定要赋值给最长子序列长度，不然如果最后一个小于前一个数，则不会进loop, 则dp[-1]不是最大值
                result = dp[i]
        return result


s = Solution()
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
