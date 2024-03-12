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


class Solution3:
    def get_max_random_index(self, nums):
        """
        Time O(n)
        Space O(1)
        随机抽取一组数列里面的最大数的index，并且如果有同样的数，保证抽到的概率一样。
        此题是Meta面试原题，这里还是运用水塘抽样算法，target值从随机一个值变成了最大值。
        """
        max_value = float('-inf')
        max_index = -1

        count = 0

        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                max_index = i
                count = 1
            else:
                count += 1
                if random.randint(1, count) == 1:
                    max_index = i

        return max_index


nums = [1, 2, 3, 3, 3]
obj = Solution2(nums)
print(obj.pick(3))
print(obj.pick(1))
print(obj.pick(3))
