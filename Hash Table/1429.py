from collections import OrderedDict


class FirstUnique:
    """O(k) time in init, O(1) in show and add, O(k) space"""
    def __init__(self, nums: [int]):
        self.unique = {}
        self.queue = OrderedDict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:

        if self.queue:
            return next(iter(self.queue))

        return -1

    def add(self, value: int) -> None:
        if value not in self.unique:
            self.unique[value] = True
            self.queue[value] = None
        elif self.unique[value]:
            self.unique[value] = False
            self.queue.pop(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)