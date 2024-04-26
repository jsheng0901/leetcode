from sortedcontainers import SortedList
from collections import deque


class MKAverage:

    def __init__(self, m: int, k: int):
        """
        Space O(m)
        双向列队存储数据流，记录顺序。sortedList记录数据大小顺序，三个指针记录最新M个数字总和，前k个总和，后k个总和。
        """
        self.m, self.k = m, k
        self.deque = deque()
        self.sl = SortedList()
        self.total = 0
        self.first_k = 0
        self.last_k = 0

    def addElement(self, num: int) -> None:
        """
        Time O(log(m))
        只有对sortedList的操作，同时维护三个指针。
        """
        # 记录总和
        self.total += num
        # 入列队
        self.deque.append(num)
        # 返回即将加入的这个数在有序list里面的index，这样同一个值的话会排在左边
        index = self.sl.bisect_left(num)

        # 如果插入值会在前k个数里面
        if index < self.k:
            # 更新指针
            self.first_k += num
            # 如果此时有序list已经大于等于k，说明插入这个数一定会移动走当前在前k里面的最后面的一个数
            if len(self.sl) >= self.k:
                # 删除被移动走的前k个的最后一个数
                self.first_k -= self.sl[self.k - 1]

        # 同上，如果插入值会在后k个数里面
        if index >= len(self.sl) + 1 - self.k:
            # 更新指针
            self.last_k += num
            # 如果此时有序list已经大于等于k，说明插入这个数一定会移动走当前在后k里面的最前面的一个数
            if len(self.sl) >= self.k:
                # 删除被移动走的后k个的最前面一个数
                self.last_k -= self.sl[-self.k]

        # 更新有序list
        self.sl.add(num)

        # 如果当前列队大于m，说明要删除最早的数
        if len(self.deque) > self.m:
            # 弹出最开始的数
            num = self.deque.popleft()
            # 更新指针
            self.total -= num
            # 找到弹出的数的index
            index = self.sl.index(num)

            # 如果弹出数在前k个里面
            if index < self.k:
                # 更新指针
                self.first_k -= num
                # 加入新的下一个进入前k个位置的数
                self.first_k += self.sl[self.k]
            # 如果弹出数在后k个里面
            elif index >= len(self.sl) - self.k:
                # 更新指针
                self.last_k -= num
                # 加入新的下一个进入后k个位置的数
                self.last_k += self.sl[-self.k - 1]

            # 更新有序list
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        """
        Time O(1)
        average等于总和 - 前后k 然后计算平均数
        """
        if len(self.sl) < self.m:
            return -1

        # 三个指针直接计算
        return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)


obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
print(obj.calculateMKAverage())
obj.addElement(10)
print(obj.calculateMKAverage())
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
print(obj.calculateMKAverage())
