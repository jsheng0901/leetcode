class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.In = []
        self.Out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.In.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 只有当Out为空的时候，再从In里导入数据（导入In全部数据）
        if len(self.Out) == 0:
            # 从In导入数据直到In为空
            while len(self.In) > 0:
                self.Out.append(self.In.pop())

        return self.Out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        front = self.pop()
        self.Out.append(front)

        return front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 此时需要判断两个是否都同时为空，因为判断一个不能说明都pop了所有元素

        return len(self.In) == 0 and len(self.Out) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)