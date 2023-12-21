from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        """
        Time O(1)
        Space O(n)
        双向列队，虽然这里只用到了双向列队的左边弹出，但是双向列队deque popleft 的 time 是 O(1)。所以整体是 O(1)。
        思路很简单，一个控制一个固定size的双向列队，新的来了就弹出列队头，更新当前总和和数据个数。
        """
        self.count += 1
        if len(self.queue) >= self.size:
            self.sum -= self.queue.popleft()

        self.sum += val
        self.queue.append(val)

        return self.sum / min(self.count, self.size)


obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
