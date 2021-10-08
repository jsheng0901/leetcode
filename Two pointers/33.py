class Solution:
    def search(self, nums: [int], target: int) -> int:
        """
        此题一定要考虑两种大情况，每种大情况下有两个小情况，见注释
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 落在同一数组的情况，同时落在数组1 或 数组2,
            # 找mid落在数组那一边的情况的情况大分类先
            if nums[mid] >= nums[left]:
                # target 落在 left 和 mid 之间，则移动我们的right，完全有序的一个区间内查找
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                # target 落在right和 mid 之间，有可能在数组1，也有可能在数组2
                elif target > nums[mid] or target < nums[left]:
                    left = mid + 1
            # 不落在同一数组的情况，left 在数组1， mid 落在 数组2
            else:
                # 有序的一段区间，target 在 mid 和 right 之间
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # 两种情况，target 在left 和 mid 之间 或者 target在左边更大的数组那边
                elif target < nums[mid] or target > nums[right]:
                    right = mid - 1

        return -1



