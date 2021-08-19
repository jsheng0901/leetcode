import random


class Solution:

    def __init__(self, w: [int]):
        self.pre_sum = []
        pre_sum = 0
        for weight in w:
            pre_sum += weight
            self.pre_sum.append(pre_sum)

        self.total_sum = pre_sum

    def pickIndex(self) -> int:
        """先构建pre_sum, 也就在每个数可能被pick的probability， 然后binary search这个pre_sum，找到target对应的最小index"""
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

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()