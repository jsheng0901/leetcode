from collections import defaultdict
import random
from typing import List


class Solution1:

    def __init__(self, nums: [int]):
        """
        Time O(n)
        Space O(n)
        """
        self.mapping = defaultdict(list)
        for i in range(len(nums)):
            self.mapping[nums[i]].append(i)

    def pick(self, target: int) -> int:
        """
        Time O(1)
        Space O(1)
        initial的时候构建hash map存储具体数字对应的index的list，pick的时候random选一个index。这里需要额外的空间来存储index。
        """
        index = self.mapping[target]
        return random.choice(index)


class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.rand = random.Random()

    def pick(self, target: int) -> int:
        """
        Time O(n)
        Space O(1)
        不需要额外的空间来构建hash table，这里用到水塘抽样算法，就是解决如何在长度未知的序列（数据流）中随机选择一个元素的数学技巧。
        当你遇到第 i 个元素时，应该有 1/i 的概率选择该元素，1 - 1/i 的概率保持原有的选择。
        """
        count, res = 0, -1
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue
            count += 1
            # 随机生成的概率等于1的情况下就是我们选择遇到第i个元素为概率 1/i 的情况
            if self.rand.randint(1, count) == 1:
                res = i
        return res


nums = [1, 2, 3, 3, 3]
obj = Solution2(nums)
print(obj.pick(3))
print(obj.pick(1))
print(obj.pick(3))

