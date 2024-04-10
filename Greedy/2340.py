from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        贪心策略，先考虑只移动找到最小值，再考虑只移动找到最大值。两边同时移动，当出现交集的时候，会少一步，如果没有交集直接相加。
        局部最优单一移动，最后全局最优。
        """
        max_index = 0
        max_value = float('-inf')
        min_index = 0
        min_value = float('inf')

        # 找到最大值和最小值对应的index，这里有个trick就是最大值如果出现相等的情况下找最靠近右边的index
        for i, v in enumerate(nums):
            if v >= max_value:
                max_value = v
                max_index = i
            if v < min_value:
                min_value = v
                min_index = i

        # 计算最大和最小的走的步数
        max_swap = len(nums) - 1 - max_index
        min_swap = min_index - 0

        # 如果没有交集，直接返回总步数
        if max_index >= min_index:
            return max_swap + min_swap
        # 如果有交集，少一步
        else:
            return max_swap + min_swap - 1


s = Solution()
print(s.minimumSwaps(nums=[3, 4, 5, 5, 3, 1]))
