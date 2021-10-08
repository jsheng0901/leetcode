class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        """
        O(n) time
        此题可以左右指针是因为原来的input就是有序的，无序的话，不能这样做
        双指针，左右指针，如果右边大就把右边插入倒叙遍历的index位置，反之左边插入，同时移动对应的左右指针
        """
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right] ** 2
                right -= 1      # 右边移动
            else:
                square = nums[left] ** 2
                left += 1       # 左边移动

            res[i] = square

        return res
