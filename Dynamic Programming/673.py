from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n)
        我们需要维护两个数组，定义分别是：
            1. dp[i]：i之前（包括i）最长递增子序列的长度为dp[i]
            2. count[i]：以nums[i]为结尾的字符串，最长递增子序列的个数为count[i]
        此题是300的衍生题目，需要记录最长子序列长度的同时，还需要记录同样index下的最长子序列个数。
        """
        dp = [1] * len(nums)
        count = [1] * len(nums)
        max_length = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:  # 说明找到了一个更长地递增子序列
                        dp[i] = dp[j] + 1  # 更新dp
                        count[i] = count[j]  # 说明新的子序列个数等于找到j结尾的子序列个数
                    elif dp[j] + 1 == dp[i]:  # 说明找到了两个相同长度的递增子序列
                        count[i] += count[j]  # 以i为结尾的子串的最长递增子序列的个数就应该加上以j为结尾的子串的个数
                max_length = max(max_length, dp[i])  # 记录最长递增子序列的最长长度

        # 要从小loop一遍dp数组找到全部等于最长子序列长度对应count数组
        # 同时把最长递增序列长度对应的count[i]累计下来就是结果了。
        result = 0
        for i in range(len(dp)):
            if dp[i] == max_length:
                result += count[i]

        return result


s = Solution()
print(s.findNumberOfLIS(nums=[1, 3, 5, 4, 7]))
