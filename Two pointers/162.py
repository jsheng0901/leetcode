class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        """
        Time O(log(n))
        Space O(1)
        双指针二分法变体，查找此点是不是在下降的趋势上，如果是下降的趋势，说明peak在左边并包含此点，如果不是下降的趋势，说明peak在右边。
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # 下一个比当前的小，说明peak在左边包含当前点
            if nums[mid] > nums[mid + 1]:
                right = mid
            # 下一个比当前的大，说明peak在右边并且当前数字不可能是peak
            else:
                left = mid + 1

        # 出循序的时左指针表示peak
        return left


s = Solution()
print(s.findPeakElement(nums=[1, 2, 3]))
print(s.findPeakElement(nums=[3, 2, 1]))
print(s.findPeakElement(nums=[1, 2, 3, 4, 2]))
