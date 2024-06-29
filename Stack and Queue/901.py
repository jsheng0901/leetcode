class StockSpanner:

    def __init__(self):
        """
        Space O(n)
        """
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        """
        Time O(1)
        对于一个固定数组，此题是找下一个更大的元素的应用。
        单调递减栈的应用，栈内存储当前元素的值和当前的index也就是第几天。这里用一个全局参数记录当前天数。遇到栈顶小于等于当前元素的就直接
        直接弹出，栈内只存储递减元素。栈顶为更大的元素对应的第几天，当前第几天直接相减得到答案。
        """
        # 累计记录当前天数
        self.day += 1

        # 栈顶小于等于当前元素，就弹出，维护单调递减栈
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        # 如果没有栈了，前一天就是第0天
        if not self.stack:
            prev_day = 0
        # 如果栈内还有元素，前一天为栈顶元素
        else:
            prev_day = self.stack[-1][1]

        # 当前元素入栈
        self.stack.append((price, self.day))
        # 返回两个天数的差值即为连续天数
        return self.day - prev_day


obj = StockSpanner()
print(obj.next(price=100))
print(obj.next(price=80))
print(obj.next(price=60))
print(obj.next(price=70))
print(obj.next(price=60))
print(obj.next(price=75))
print(obj.next(price=85))
