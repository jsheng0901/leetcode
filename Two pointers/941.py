from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Time O(n)
        Space O(1)
        双指针写法，左右指针遍历，如果最后都走到一起，则说明有山峰
        """
        if len(arr) < 3:
            return False

        left = 0
        right = len(arr) - 1
        # 防止左指针越界
        while left < len(arr)-1 and arr[left + 1] > arr[left]:
            left += 1
        # 防止右指针越界
        while right > 0 and arr[right - 1] > arr[right]:
            right -= 1

        # 检查是否是单调数组，左右是否都走到底了
        if left == len(arr) - 1:
            return False
        if right == 0:
            return False

        return left == right


s = Solution()
print(s.validMountainArray(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
