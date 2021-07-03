class Solution:
    def lower(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def upper(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right

    def searchRange(self, nums: [int], target: int) -> [int]:
        """
        此处和普通二分法不一样的主要是等于的情况也要考虑进去，这样才可以找到两边的最小和最大的边界
        :param nums:
        :param target:
        :return:
        """
        upper = self.upper(nums, target)
        lower = self.lower(nums, target)

        if upper < lower:
            return [-1, -1]
        else:
            return [lower, upper]
