import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False

        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_element = self.list[-1]        # 找到最后一个元素
            index = self.dict[val]              # 找到要移除元素的index
            self.list[index] = last_element     # 把最后一个元素放到要移除元素的index上面，此时list里面已经没有要移除的元素
            self.dict[last_element] = index     # 更新最后一个元素对应的新的index在dictionary里面
            self.list.pop()                     # 弹出最后一个元素，因为已经把这个元素放进了要移除的index的位置，重复的要移除
            del self.dict[val]                  # 删除dictionary里面要移除元素的key
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return random.choice(self.list)         # 随机选择一个在list里面

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()