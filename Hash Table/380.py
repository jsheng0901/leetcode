import random


class RandomizedSet:

    def __init__(self):
        """
        Space O(n)
        """
        self.nums = []  # 存储元素的值
        self.val_to_index = dict()  # 记录每个元素对应在 nums 中的索引

    def insert(self, val: int) -> bool:
        """
        Time O(1)
        """
        # 若 val 已存在，不用再插入
        if val in self.val_to_index:
            return False
        # 若 val 不存在，插入到 nums 尾部，
        # 并记录 val 对应的索引值
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Time O(1)
        """
        # 若 val 不存在，不用再删除
        if val not in self.val_to_index:
            return False
        # 先拿到 val 的索引
        index = self.val_to_index[val]
        # 将最后一个元素对应的索引修改为 index
        self.val_to_index[self.nums[-1]] = index
        # 交换 val 和最后一个元素
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # 在数组中删除元素 val
        self.nums.pop()
        # 删除元素 val 对应的索引
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        """
        Time O(1)
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
