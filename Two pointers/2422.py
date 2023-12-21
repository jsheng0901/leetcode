from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        双指针 + 贪心，左右同时check左右两边是否相等，如果不相等，merge小的那一边，并走一步，并记录一次merge的结果，
        如果相等则左右同时走一步。
        """
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            # 左右相等，各自走一步
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            # 左边更小
            elif nums[left] < nums[right]:
                # 左边走一步
                left += 1
                # 同时更新左边走完后的merge之后的结果
                nums[left] = nums[left] + nums[left - 1]
                # 记录一次操作
                res += 1
            # 右边更新，同上
            elif nums[left] > nums[right]:
                right -= 1
                nums[right] = nums[right] + nums[right + 1]
                res += 1

        # 返回操作次数
        return res


s = Solution()
print(s.minimumOperations(nums=[1, 2, 3, 4]))
print(s.minimumOperations(nums=[4, 3, 2, 1, 2, 3, 1]))
