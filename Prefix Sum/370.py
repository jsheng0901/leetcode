from typing import List


class Difference:
    def __init__(self, nums: List[int]):
        """
        Time O(n)
        Space O(n)
        构建差分数组，差分数组公式 diff[i] = nums[i] - nums[i - 1]
        """
        assert len(nums) > 0
        # 差分数组
        self.diff = [0] * len(nums)
        # 根据初始数组构造差分数组
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            # diff的公式 nums[i] - nums[i - 1] = diff[i]
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i: int, j: int, val: int) -> None:
        """
        Time O(1)
        Space O(1)
        只需要对两个数进行加减
        """
        # 给闭区间 [i, j] 增加 val（可以是负数
        self.diff[i] += val
        # 这里要判断一下，如果 j + 1 > 总长度，说明 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        """
        Time O(n)
        Space O(1)
        重新构建回去数组，根据差分数组的结果
        """
        # 返回结果数组
        res = [0] * len(self.diff)
        # 根据差分数组构造结果数组
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            # diff的公式 nums[i] - nums[i - 1] = diff[i]
            res[i] = res[i - 1] + self.diff[i]

        return res


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        差分数组的典型应用，对一个区间频繁的增减，可以把时间降低到每次只需要O(1)的时间复杂度，最后复原的时候才需要O(n)。
        """
        nums = [0] * length
        # 构建差分数组
        difference = Difference(nums)
        # 对这个数组进行所有的更新
        for update in updates:
            i, j, val = update[0], update[1], update[2]
            difference.increment(i, j, val)

        # 返回所有更新后的结果
        return difference.result()


s = Solution()
print(s.getModifiedArray(length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
