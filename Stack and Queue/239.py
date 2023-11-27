from typing import List


class Deque:
    """
    单调列队，两边都可以进或者出，但是保证deque是从左到右单调递减
    """

    def __init__(self):
        """
        Time O(1)
        Space O(n)
        """
        self.deque = []

    def pop(self, value):
        """
        Time O(1)
        """
        # 每次弹出时候，比较当前要弹出的数值时候等于queue出口元素的数值，如果相等则弹出
        if len(self.deque) > 0 and value == self.deque[0]:
            self.deque.pop(0)

    def push(self, value):
        """
        Time O(1)
        """
        # 如果push的数值大于元素入口的数值，那么就将deque最后端的数值弹出，直到push的数值小于等于deque入口元素
        # 这样就保证了deque里面的数值永远是单带从大到小的排序
        while len(self.deque) > 0 and value > self.deque[-1]:
            self.deque.pop()

        self.deque.append(value)

    def get_front(self):
        """
        Time O(1)
        """
        return self.deque[0]


class Solution1:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        """
        Time O(n)
        Space O(n)
        滑动窗口，用deque来实现记录最大值
        """
        deque = Deque()
        result = []

        for i in range(k):  # 先将前K个数字放进deque里面
            deque.push(nums[i])

        result.append(deque.get_front())   # 记录最开始的前K个数字中最大的数值

        for j in range(k, len(nums)):
            deque.pop(nums[j - k])  # 移除滑动窗口的第一个数字
            deque.push(nums[j])
            result.append(deque.get_front())

        return result


class MonotonicQueue:
    def __init__(self):
        self.maxq = []

    def push(self, n):
        # 将小于 n 的元素全部删除
        while self.maxq and self.maxq[-1] < n:
            self.maxq.pop()
        # 然后将 n 加入尾部
        self.maxq.append(n)

    def max(self):
        return self.maxq[0]

    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.pop(0)


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time O(n)
        Space O(n)
        同上的方法，只是换一种写单调列队的方式。
        """
        window = MonotonicQueue()
        res = []

        for i in range(len(nums)):
            if i < k - 1:
                # 先填满窗口的前 k - 1
                window.push(nums[i])
            else:
                # 窗口向前滑动，加入新数字
                window.push(nums[i])
                # 记录当前窗口的最大值
                res.append(window.max())
                # 移出旧数字
                window.pop(nums[i - k + 1])
        return res


s = Solution2()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
