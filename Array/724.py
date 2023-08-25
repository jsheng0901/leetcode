from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        找到中间index刚好是左右数组和相等的点，则说明找到了pivot。
        """
        total = sum(nums)   # 数组总和

        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - nums[i] - left_sum:  # 左右和相等
                return i
            left_sum += nums[i]

        return -1
