class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []    # 备份用

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # loop q1 and remove all element expect last one to q2, and add to q2
        size = len(self.q1)
        while size > 1:
            self.q2.append(self.q1.pop(0))
            size -= 1

        # 此时q1之剩下一个元素并且为最top的元素，也就是我们需要的结果
        result = self.q1.pop()
        # 复制q2给q1, 此处不能直接等于，因为l1会受l2影响
        # 清空q2
        while self.q2:
            self.q1.append(self.q2.pop(0))

        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
print(param_2)
param_3 = obj.pop()
print(param_3)
param_4 = obj.empty()
print(param_4)