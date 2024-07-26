from typing import List


class Difference:
    def __init__(self, nums: List[int]):
        """
        Time O(n)
        Space O(n)
        差分数组，差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减。
        """
        self.diff = [0] * len(nums)
        # 根据初始数组构造差分数组
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i: int, j: int, val: int) -> None:
        """
        Time O(1)
        Space O(1)
        给闭区间 [i, j] 增加 val（可以是负数）,
        只要花费 O(1) 的时间修改 diff 数组，就相当于给 nums 的整个区间做了修改。多次修改 diff，
        然后通过 diff 数组反推，即可得到 nums 修改后的结果。
        """
        self.diff[i] += val
        # 当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了。
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        """
        Time O(n)
        Space O(n)
        返回结果数组
        """
        result = [0] * len(self.diff)
        # 根据差分数组构造结果数组
        result[0] = self.diff[0]
        for i in range(1, len(result)):
            result[i] = result[i - 1] + self.diff[i]

        return result


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        Time O(n)
        Space O(n)
        典型的差分数组的应用，bookings里面存在频繁的对最终数组区间的增删value。
        """
        # nums 初始化为全 0
        nums = [0] * n
        # 构造差分解法
        df = Difference(nums)

        for booking in bookings:
            i, j, val = booking[0], booking[1], booking[2]
            # 对区间 nums[i-1...j-1] 增加 val，index要减1因为booking是1base的index
            df.increment(i - 1, j - 1, val)

        # 返回最终的结果数组
        result = df.result()

        return result


s = Solution()
print(s.corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
