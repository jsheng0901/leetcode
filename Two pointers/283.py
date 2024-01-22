class Solution1:
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


class Solution2:
    def moveEvens(self, nums: [int]) -> None:
        """
        Time O(n)
        Space O(1)
        双指针思路，和27题移动target数值一模一样，只是这里target是偶数，本质上遇到要移除的情况才swap指针。
        """

        p1 = 0

        for p2 in range(len(nums)):
            # 遇到不是偶数的时候，开始swap，并移动慢指针。
            if nums[p2] % 2 != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

        return nums[:p1]


class Solution3:
    def moveZeroesLeft(self, nums: [int]) -> None:
        """
        Time O(n)
        Space O(1)
        双指针思路，和上面的思路一样，只是移动到左边，那么我们从后向前遍历即可，注意慢指针的起始位置要设置到最后一位。
        """

        p1 = len(nums) - 1

        for p2 in range(len(nums) - 1, -1, -1):
            # 遇到不等于的时候，开始swap，并移动慢指针，注意这里慢指针是减1。
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 -= 1

        return nums


s = Solution1()
print(s.moveZeroes(nums=[0, 1, 0, 3, 12]))

s = Solution2()
print(s.moveEvens(nums=[0, 1, 0, 3, 12]))

s = Solution3()
print(s.moveZeroesLeft(nums=[0, 1, 0, 3, 12]))
