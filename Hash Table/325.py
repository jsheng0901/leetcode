from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(n)
        和560一模一样的思路，只是这里是计算最早出现的前缀和的index。
        """
        n = len(nums)
        # pre_sum 中的值 -> 对应的最小索引
        # 比如 pre_sum = [2,4,1,3,4] pre_sum_to_index[4] = 1
        pre_sum_to_index = {}
        max_len = 0
        # 前缀和数组（在这道题中可以优化为一个变量）
        pre_sum = 0
        # base case，这样索引相减的时候可以算出正确的子数组长度
        pre_sum_to_index[0] = -1
        for i in range(n):
            # 计算前缀和，维护 preSum = sum(nums[0..i])
            pre_sum += nums[i]
            # 确保 pre_sum_to_index 中记录的索引是第一次出现的位置，setdefault会拿到出现的value如果不存在则设置为插入的value
            pre_sum_to_index.setdefault(pre_sum, i)
            need = pre_sum - k
            if need in pre_sum_to_index:
                j = pre_sum_to_index[need]
                # nums[j..i] 是和为 k 的子数组
                max_len = max(max_len, i - j)

        return max_len


s = Solution()
print(s.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
print(s.maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))
