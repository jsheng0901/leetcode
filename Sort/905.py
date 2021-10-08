class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
        """
        quick sort, if (1, 0) then swap, if (1, 1) only right is correct then right -1,
        if (0, 0) only left is correct then left + 1
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            elif nums[left] % 2 == 0:
                left += 1

            elif nums[right] % 2 == 1:
                right -= 1

        return nums
