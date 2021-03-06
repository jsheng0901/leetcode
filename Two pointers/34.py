class Solution1:
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


# 解法2
# 1、首先，在 nums 数组中二分查找 target；
# 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
# 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间
class Solution2:
    def searchRange(self, nums: [int], target: int) -> [int]:
        def binarySearch(nums: [int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:  # 不变量：左闭右闭区间
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1

        index = binarySearch(nums, target)
        if index == -1: return [-1, -1]  # nums 中不存在 target，直接返回 {-1, -1}
        # nums 中存在 targe，则左右滑动指针，来找到符合题意的区间
        left, right = index, index
        # 向左滑动，找左边界
        while left - 1 >= 0 and nums[left - 1] == target: left -= 1
        # 向右滑动，找右边界
        while right + 1 < len(nums) and nums[right + 1] == target: right += 1
        return [left, right]
