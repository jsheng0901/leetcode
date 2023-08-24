from typing import List


class Solution1:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: [int], k: int) -> None:
        """
        Time O(n)
        Space O(1)
        k 需要先除以长度，计算余数，因为k可能超过数组的长度，会出现重复循环的旋转
        """
        k %= len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        return nums


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Time O(n * k) 每一次insert都要移动整个数组
        Space O(1)
        弹出尾巴，然后insert进开始
        """
        for i in range(k):
            element = nums.pop()
            nums.insert(0, element)

        return nums


s = Solution2()
print(s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
