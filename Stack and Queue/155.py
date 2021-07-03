class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []     # 构建单调递减stack

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack_min) == 0 or self.stack_min[-1] >= val:   # 如果push进来的数字小于最后一个，则加入
            self.stack_min.append(val)

    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.stack_min[-1]:       # 如果pop出去的刚好是最小值，则单调stack也要pop掉最小值
            self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()