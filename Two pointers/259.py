from typing import List


class Solution:
    def two_sum_smaller(self, nums, left, right, target):
        # 计数
        count = 0
        while left < right:
            # 当左右指针小于target时候
            if nums[left] + nums[right] < target:
                # nums[left] 和 nums[left+1..right]
                # 中的任一元素之和都小于 target
                # 记录区间内有多少和左指针的组合，其实就是区间长度
                count += right - left
                left += 1
            # 大于等于的时候，移动右指针
            else:
                right -= 1

        return count

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Time O(n * log(n) + n^2)
        Space O(1)
        三个数之和的变体，逻辑都是一样的，先sort一下顺序，固定第一个数，对剩下的数组做双指针搜索。这里不需要查重的过程，因为我们是计次数，
        不是记录三个数的结果，详细见注释。
        """
        # 先从小到大sort一下
        nums.sort()
        res = 0
        # 每个数作为第一个数
        for i in range(len(nums) - 2):
            # 固定 nums[i] 为三数之和中的第一个数，
            # 然后对 nums[i+1..] 搜索小于 target - nums[i] 的两数之和个数
            first = nums[i]
            # 左右指针
            left = i + 1
            right = len(nums) - 1
            # 找到剩下的数组部分小于target的个数
            res += self.two_sum_smaller(nums, left, right, target - first)

        return res


s = Solution()
print(s.threeSumSmaller(nums=[-2, 0, 1, 3], target=2))
print(s.threeSumSmaller(nums=[0], target=0))
