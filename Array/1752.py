from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Time O(n)
        Space O(1)
        是否可以旋转后保证递增，其实就是查看有多少个峰值点，小于等于1个峰值点都可以，注意这里需要判断一下最后一个数和第一个数的大小，
        如果最后一个数大于第一个数，那么最后一个数也是一个峰值点旋转后。
        """
        num_peak = 0
        for i in range(len(nums)):
            # 如果不是最后一个数，当前一个大于后一个数，找到一个峰值点
            if i != len(nums) - 1 and nums[i] > nums[i + 1]:
                num_peak += 1
            # 如果是最后一个数，最后一个数大于第一个数，找到一个峰值点
            if i == len(nums) - 1 and nums[i] > nums[0]:
                num_peak += 1

        # 判断数量是否小于等于1
        return num_peak <= 1


s = Solution()
print(s.check(nums=[3, 4, 5, 1, 2]))
print(s.check(nums=[2, 1, 3, 4]))
print(s.check(nums=[1, 2, 3]))
