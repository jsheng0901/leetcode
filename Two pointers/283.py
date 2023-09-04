class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Time O(n)
        Space O(1)
        双指针思路，和27题移动target数值一模一样，只是这里target是0
        """

        p1 = 0

        for p2 in range(len(nums)):
            # 遇到不等于的时候，开始swap，并移动慢指针。
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

        return nums


s = Solution()
print(s.moveZeroes(nums=[0, 1, 0, 3, 12]))
