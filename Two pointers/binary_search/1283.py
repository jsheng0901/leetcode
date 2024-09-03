import math
from typing import List


class Solution:
    def get_sum_division(self, nums, mid):
        res = 0
        for num in nums:
            res += math.ceil(num / mid)

        return res

    def left_bound_search(self, nums, threshold):
        # 初始化的两个左右指针，只需要在在最大值区间内查找，因为取最大值的时候，可以保证所有的除数结果都是1，此时和最小
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            # 得到所有的数除数结果和
            sum_of_division = self.get_sum_division(nums, mid)

            if sum_of_division > threshold:
                left = mid + 1
            # 注意这里移动是右指针，因为这里是单调递减函数
            elif sum_of_division == threshold:
                right = mid - 1
            elif sum_of_division < threshold:
                right = mid - 1

        # 返回左指针，因为题目找的是小于等于threshold的情况
        return left

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        Time O(n * log(m))  m -> max number in nums
        Space O(1)
        此题明显的二分法思路，随着除数的增加，除数的结果和会逐渐递减，所以这个是个单调递减函数上找最接近threshold的左边界x值。详细见注释。
        """
        # 找左边界写法
        left = self.left_bound_search(nums, threshold)

        return left


s = Solution()
print(s.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
print(s.smallestDivisor(nums=[44, 22, 33, 11, 1], threshold=5))
