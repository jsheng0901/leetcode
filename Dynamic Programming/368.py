from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Time O(nlog(n) + n^2)
        Space O(n)
        动态规划，dp[i]表示以i结尾的nums[i]最长符合题目要求的subset的长度，prev[i]表示符合最长长度的当前nums[i]的前一个的index，
        我们每次找到最长subset的长度，并且存储起来最长subset用到的前一个的index，同时存储最长长度的结尾index，最后从后往前加入result。
        """
        # 先sort一下，只用判断nums[i] % nums[j]
        nums.sort()

        # 初始化dp数组都是1，因为就自己为一个subset时候最小是1
        dp = [1] * len(nums)
        # 初始化index数组，任意不小于0的值都可以
        prev = [-1] * len(nums)

        # 记录最长的subset的长度和终止index
        max_size = 1
        max_index = 0

        for i in range(1, len(nums)):
            for j in range(i):
                # 如果符合条件，并且当前nums[i]和nums[j]组成的subset长度大于之前的情况
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    # 更新dp[i]，并且记录此时满足最长subset用到的前一个index j
                    dp[i] = dp[j] + 1
                    prev[i] = j

            # 如果找到最大值长度，记录此时终止位置index i
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        result = []
        # 从后往前开始加入结果result，最终subset的起始位置的index在prev里面一定是初始值，因为只有这个数自己，此时就是初始值。
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        # 倒序返回，因为是从后往前加入的result
        return result[::-1]


s = Solution()
print(s.largestDivisibleSubset(nums=[4, 8, 10, 240]))
