from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        """
        Time O(n)
        Space O(n)
        前缀和主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和。
        初始化前缀和数组，pre_sum[i] 记录 nums[0..i-1] 的累加和
        """
        # 前缀和数组
        self.pre_sum = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(self.pre_sum)):
            self.pre_sum[i] = self.pre_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        """
        Time O(1)
        Space O(1)
        搜索时间永远是直接计算，简化到O(1)
        """
        return self.pre_sum[right + 1] - self.pre_sum[left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
