import heapq


class MedianFinder:

    def __init__(self):
        """
        Time O(1)
        Space O(n)
        """
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        """
        Time O(5 * log(n) -> log(n))
        Space O(n)
        此题的核心点是，对于中位数，两种情况：
        1. 偶数，中位数由前半部分的最大值和后半部分最小值计算平均值得来
        2. 技术，中位数由前半部分的最大值得来
        所以我们可以构建一个前半部分的大顶堆，和后半部分的小顶堆。保证大顶堆的最大值小于等于小顶堆的最小值，并且大顶堆的大小永远大于等于小顶堆。
        也就是说如果是偶数，先去大顶堆，再去小顶堆保证两边大小相等。
        如果是奇数，还是先去大顶堆，再去小顶堆，再回去大顶堆，保证大顶堆头是最大值同时是中位数。
        """
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        # 先去大顶堆
        heapq.heappush(self.max_heap, (-num, num))
        # 弹出大顶堆中的最大值
        _, max_heap_top = heapq.heappop(self.max_heap)
        # 再去小顶堆上面弹出的最大值
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count % 2 == 1:
            # 弹出小顶堆
            min_heap_top = heapq.heappop(self.min_heap)
            # 从新回到大顶堆
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self) -> float:
        """
        Time O(1)
        Space O(n)
        """
        if self.count % 2 == 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.max_heap[0][1] + self.min_heap[0]) / 2


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
