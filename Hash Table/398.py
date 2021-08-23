from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: [int]):
        self.mapping = defaultdict(list)
        for i in range(len(nums)):
            self.mapping[nums[i]].append(i)

    def pick(self, target: int) -> int:
        """
        O(n) time initial, O(1) time pick, O(n) space
        initial的时候构建hash map存储具体数字对应的index的list，pick的时候random选一个index
        """
        index = self.mapping[target]
        # if len(index) == 1:
        #     return index[0]
        # else:
        return random.choice(index)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)