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


class Solution2:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Time O(nlog(n) + n^2)
        Space O(n^2)
        先排序，排序后此题就变成了寻找一个最长递增子序列，且要求每个元素都能够整除前面那个元素。
        定义：dp[i] 表示以 nums[i] 这个数结尾的最长符合要求的子序列本身。
        用找最长递增子序列的方法，当找到符合整除的数的时候，判断一下前面的子序列的长度是否大于最大子序列，如果大于则更新长度和当前index。
        如果此时index不是初始值，说明有更长的子序列出现，当前子序列扩充为前面的子序列 + 当前自己。
        """
        # 先排序
        nums.sort()
        # 构建dp，根据定义
        dp = [[] for _ in range(len(nums))]
        # 初始化dp[0]，包含第一个数字本身
        dp[0].append(nums[0])

        for i in range(1, len(nums)):
            # 当前最长长度，和初始化index
            max_sub_length = 0
            index = -1
            # 在 nums[0..i-1] 中寻找那个 nums[i] 能接到结尾的最长子序列
            for j in range(i):
                # 如果出现符合条件的数，更新最长长度和符合条件的时候的index
                if nums[i] % nums[j] == 0 and len(dp[j]) > max_sub_length:
                    max_sub_length = len(dp[j])
                    index = j

            # nums[0..i-1] 中最长的那个子序列，也就是上面找到的index位置，再加上 nums[i]，
            # 就是 nums[0..i] 最长的子序列，存储子序列本身进当前dp[i]的位置
            if index != -1:
                dp[i].extend(dp[index])
            # 无论有没有更长的子序列，当前dp[i]都至少包含自己作为最长子序列
            dp[i].append(nums[i])

        # 至少有1个长度，初始值
        res = dp[0]
        # 找到全局中最长的子序列本身，loop一遍dp数组找最长即可
        for i in range(1, len(dp)):
            if len(res) < len(dp[i]):
                res = dp[i]
        return res


s = Solution2()
print(s.largestDivisibleSubset(nums=[4, 8, 10, 240]))
print(s.largestDivisibleSubset(nums=[1, 2, 4, 8]))
