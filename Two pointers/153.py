class Solution:
    def findMin(self, nums: [int]) -> int:
        """
        同二分法查找，只是判断每次判断是否在同一个单调递增区间，移动右指针的时候不能 mid - 1， 因为有可能mid在最小值，否则就漏掉了最小值
        但是mid永远是向下取整，所以left可以+1，因为mid不会是最小值
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[right]:
                return nums[left]

            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
