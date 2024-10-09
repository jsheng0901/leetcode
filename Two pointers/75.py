class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Time O(n)
        Space O(1)
        三指针思路，把1最为pivot值，另外两个一直交换，当交换2的时候我们还要继续判断一下i所在的index是否符合顺序，所以遇到2的时候交换完，
        只有2的指针移动，cur指针不动。
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            # 移动两个指针
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            # 只移动2的指针
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

        return nums


s = Solution()
print(s.sortColors(nums=[2, 0, 2, 1, 1, 0]))
print(s.sortColors(nums=[2, 0, 1]))
