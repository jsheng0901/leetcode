from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        找一个循环数组的最大subarray，并且不能出现重复的同一个数在这个subarray里面，有两种情况，
        第一种是最大subarray出现在[i, .. n-1]之间，就是没有循环一头一尾出现
        第二种是最大subarray出现在[i, .. n-1, i, .., n-1]之间，也就是一头一尾有出现在里面，这种情况我们可以计算反面，一头一尾最大，
        也就是中间最小即可，所以问题转化为，计算最大的subarray和计算最小的subarray。最后对比两种情况即可。
        """
        # 指针记录最大和最小，dp只需要一个指针，因为我只关心前一个数的dp情况
        dp_max = nums[0]
        dp_min = nums[0]
        max_num = nums[0]
        min_num = nums[0]

        for i in range(1, len(nums)):
            # 当前最大值
            dp_max = max(nums[i], nums[i] + dp_max)
            # 当前最小值
            dp_min = min(nums[i], nums[i] + dp_min)
            # 全局最大值
            max_num = max(max_num, dp_max)
            # 全局最小值
            min_num = min(min_num, dp_min)

        # 特殊情况，如果全都是负数，此时最小值会是整个数组，相见后会变成0，但是最大值一定是负数，参考测试数据3
        if max_num < 0:
            return max_num

        # 两种情况取最大值
        res = max(max_num, sum(nums) - min_num)

        return res


s = Solution()
print(s.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
print(s.maxSubarraySumCircular(nums=[5, -3, 5]))
print(s.maxSubarraySumCircular(nums=[-3, -2, -3]))
