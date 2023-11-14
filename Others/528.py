import random
from typing import List


class Solution:

    def __init__(self, w: [int]):
        """
        Time O(n)
        Space O(n)
        构建前缀和，也就在每个数可能被pick的probability
        """
        self.pre_sum = []
        pre_sum = 0
        for weight in w:
            pre_sum += weight
            self.pre_sum.append(pre_sum)

        self.total_sum = pre_sum

    def pickIndex(self) -> int:
        """
        Time O(log(n))
        Space O(1)
        找到target值，binary search这个前缀和，找到target对应的最小index
        """
        target = self.total_sum * random.random()
        left = 0
        right = len(self.pre_sum) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.pre_sum[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


class Solution2:

    def __init__(self, w: List[int]):
        self.pre_sums = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            self.pre_sums.append(cur_sum)

        self.total_sum = self.pre_sums[-1]

    def pickIndex(self) -> int:
        """
        同上思路，区别在于写二分法找左边界的标准模板写法。二分法左边界写法在不存在target值的情况下，
        保证能找大于target值的最小的那个值的index。
        """
        target = self.total_sum * random.random()
        left = 0
        right = len(self.pre_sums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.pre_sums[mid] < target:
                left = mid + 1
            elif self.pre_sums[mid] == target:
                right = mid - 1
            elif self.pre_sums[mid] > target:
                right = mid - 1

        return left


obj = Solution2(w=[1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
