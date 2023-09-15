# 二分法搜索的三种情况模板总结，全部采用左闭右闭的区间来写
# def binary_search(nums: List[int], target: int) -> int:
#     # 设置左右下标
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] == target:
#             # 找到目标值
#             return mid
#     # 没有找到目标值
#     return -1
#
# def left_bound(nums: List[int], target: int) -> int:
#     # 设置左右下标
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] == target:
#             # 存在目标值，缩小右边界
#             right = mid - 1
#     # 判断是否存在目标值，这里其实不会出现 left < 0 的情况，因为 left 初始值就是0，加这个判断只是代码好习惯
#     if left < 0 or left >= len(nums):     # 或者只写 left >= len(nums) 判断也行
#         return -1
#     # 判断找到的左边界是否是目标值，出循环的情况是 left = right + 1，所以返回 right + 1也行
#     return left if nums[left] == target else -1
#
# def right_bound(nums: List[int], target: int) -> int:
#     # 设置左右下标
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] == target:
#             # 存在目标值，缩小左边界
#             left = mid + 1
#     # 判断是否存在目标值，这里其实不会出现 right >= len(nums) 的情况，因为 right 初始值就是len(nums) - 1，加这个判断只是代码好习惯
#     if right < 0 or right >= len(nums):     # 或者只写 right < 0 判断也行
#         return -1
#     # 判断找到的右边界是否是目标值，出循环的情况是 right = left - 1，所以返回 left - 1也行
#     return right if nums[right] == target else -1

class Solution:
    def search(self, nums: [int], target: int) -> int:
        """
        Time: O(logn)
        Space: O(1)
        """

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
