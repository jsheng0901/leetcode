from collections import OrderedDict


class FirstUnique:
    def __init__(self, nums: [int]):
        """
        Time O(k)
        Space O(k)
        """
        self.unique = {}
        # 用有序字典，来记录插入字符的顺序
        self.queue = OrderedDict()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        """
        Time O(1)
        """
        # Check if there is still a value left in the queue. There might be no uniques.
        if self.queue:
            # We don't want to actually *remove* the value.
            # Seeing as OrderedDict has no "get first" method, the way that we can get
            # the first value is to create an iterator, and then get the "next" value
            # from that. Note that this is O(1).
            return next(iter(self.queue))

        return -1

    def add(self, value: int) -> None:
        """
        Time O(1)
        """
        # Case 1: We need to add the number to the queue and mark it as unique.
        if value not in self.unique:
            self.unique[value] = True
            self.queue[value] = None
        # Case 2: We need to mark the value as no longer unique and then
        # remove it from the queue.
        elif self.unique[value]:
            self.unique[value] = False
            self.queue.pop(value)


obj = FirstUnique(nums=[2, 3, 5])
print(obj.showFirstUnique())
obj.add(value=5)
print(obj.showFirstUnique())
obj.add(value=2)
print(obj.showFirstUnique())
obj.add(value=3)
print(obj.showFirstUnique())
