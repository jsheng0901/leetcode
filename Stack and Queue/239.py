class Deque:
    """单调列队，两边都可以进或者出，但是保证deque是从左到右单调递减"""

    def __init__(self):
        self.deque = []

    def pop(self, value):
        # 每次弹出时候，比较当前要弹出的数值时候等于queue出口元素的数值，如果相等则弹出
        if len(self.deque) > 0 and value == self.deque[0]:
            self.deque.pop(0)

    def push(self, value):
        # 如果push的数值大于元素入口的数值，那么就将deque最后端的数值弹出，直到push的数值小于等于deque入口元素
        # 这样就保证了deque里面的数值永远是单带从大到小的排序
        while len(self.deque) > 0 and value > self.deque[-1]:
            self.deque.pop()

        self.deque.append(value)

    def get_front(self):

        return self.deque[0]


def maxSlidingWindow(nums: [int], k: int) -> [int]:
    """
    O(n) time, 滑动窗口，用deque来实现记录最大值
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


print(maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
