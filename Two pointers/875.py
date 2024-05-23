from typing import List


class Solution:
    def f(self, piles, x):
        # 计算x的速度下要多久吃完所有香蕉
        hours = 0
        for i in range(len(piles)):
            hours += piles[i] // x
            if piles[i] % x > 0:
                hours += 1

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Time O(n * log(m))
        Space O(1)
        如果遇到一个算法问题，能够确定 x, f(x), target 分别是什么，并写出单调函数 f 的代码，那么就可以运用二分搜索的思路求解。
        这题珂珂吃香蕉的速度 K 就是自变量 x，吃完所有香蕉所需的时间就是单调函数 f(x)，target 就是吃香蕉的时间限制 H。我们需要调整 x，
        使得 f(x) 尽可能接近 target，也就是说，我们需要找到最小的 x，使得 f(x) <= target。
        """
        # 构建边界
        left = 1
        right = max(piles)
        # 标准找左边界写法
        while left <= right:
            mid = left + (right - left) // 2
            hours = self.f(piles, mid)
            # 因为这里是单调递减函数，所以小于等于目标值的时候，我们要移动的是右指针
            if hours < h:
                right = mid - 1
            elif hours == h:
                right = mid - 1
            # 大于目标值移动左指针
            else:
                left = mid + 1

        return left


s = Solution()
print(s.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
