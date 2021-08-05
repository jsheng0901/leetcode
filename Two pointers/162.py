class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        """双指针左右"""
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
