class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        """
        Time O(n^2)
        Space O(n)
        动态规划定义：位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
        """
        dp = [1] * len(nums)
        result = 1      # 初始化结果为1，因为至少有一个数

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 注意这里不是要dp[i] 与 dp[j] + 1进行比较，而是我们要取dp[j] + 1的最大值。
            # 非常重要，一定要赋值给最长子序列长度，不然如果最后一个小于前一个数，则不会进loop, 则dp[-1]不是最大值，时刻update结果
            result = max(result, dp[i])
        return result


s = Solution()
print(s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
