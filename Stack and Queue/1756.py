from sortedcontainers import SortedList


class MRUQueue1:

    def __init__(self, n: int):
        """
        Time O(n)
        Space O(n)
        """
        self.queue = []
        for i in range(n):
            self.queue.append(i + 1)

    def fetch(self, k: int) -> int:
        """
        Time O(n)
        Space O(1)
        直接用list实现，删除和添加在list里面都是O(n)的操作。
        """
        num = self.queue.pop(k - 1)
        self.queue.append(num)
        return num


class MRUQueue2:
    def __init__(self, n: int):
        """
        Time O(n)
        Space O(n)
        """
        # 存储初始化的排序用的index value和实际value
        # [(priority value index, actual value)]
        self.q = SortedList((i, i) for i in range(1, n + 1))

    def fetch(self, k: int) -> int:
        """
        Time O(log(n))
        Space O(1)
        用sortedlist来实现，存储一个tuple -> (index, value)。
        每次删除后，找到最后一个元素的index，然后我们添加删除这个元素进去，根据index来排序。
        """
        # 拿出对应index的value
        _, num = self.q.pop(k - 1)
        # 如果queue内还有元素，说明要加到队尾
        if self.q:
            # 拿出最后一个的用来排序的index值
            max_priority = self.q[-1][0]
            # 新加入的index值 +1
            self.q.add((max_priority + 1, num))
        else:
            # 如果是空队列，则直接index值为0
            self.q.add((0, num))
        return num


# Your MRUQueue object will be instantiated and called as such:
obj = MRUQueue2(8)
print(obj.fetch(3))
print(obj.fetch(5))
print(obj.fetch(2))
print(obj.fetch(8))
