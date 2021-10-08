class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        双指针思路，和移动target数值一模一样，只是这里target是0
        """

        p1 = 0

        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

