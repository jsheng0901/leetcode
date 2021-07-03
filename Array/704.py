class Solution:
    def search(self, nums: [int], target: int) -> int:
        # 遵循左闭右闭的区间写法, 此方法非常重要

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
