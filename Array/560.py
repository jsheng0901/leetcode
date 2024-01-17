class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        """
        Time O(n)
        Space O(n)
        每次记录前缀和，check pre_sum - k 是否出现过，如果出现过，意味着之前有前缀和等于rest，
        因为pre_sum1 - pre_sum2 = k 及为我们要找的区间sub-array
        """
        # 初始化difference为0的情况，因为可能从头加的pre_sum直接等于k
        pre_sum_to_freq = {0: 1}
        count = 0
        pre_sum = 0

        # 开始前缀和遍历
        for i in nums:
            pre_sum += i

            # 如果difference出现过，说明有我们需要的区间，直接累加出现过的频率
            if pre_sum - k in pre_sum_to_freq:
                count += pre_sum_to_freq[pre_sum - k]

            # 更新hash map记录前缀和出现的频率
            if pre_sum in pre_sum_to_freq:
                pre_sum_to_freq[pre_sum] += 1
            else:
                pre_sum_to_freq[pre_sum] = 1

        return count


s = Solution()
print(s.subarraySum(nums=[1, 1, 1], k=2))
