from collections import deque


class Solution:
    def traversal(self, s):
        # 同227，区别就是转换s成为双向queue来处理
        stack = []
        num = 0
        sign = "+"

        while len(s) > 0:
            c = s.popleft()
            if c.isdigit():
                num = num * 10 + (int(ord(c)) - int(ord("0")))
            # 遇到左括号开始递归计算 num
            if c == "(":
                num = self.traversal(s)
            if (c.isdigit() is False and c != " ") or len(s) == 0:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    pre = stack.pop()
                    stack.append(pre * num)
                elif sign == "/":
                    pre = stack.pop()
                    stack.append(int(pre / num))
                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ")":
                break

        return sum(stack)

    def calculate(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        同上224一模一样的逻辑，只需要添加乘法和除法的逻辑在遇到符号的时候。
        """
        # 小细节这里要用双向列队保证后面弹出左边是O(1)的操作不然普通的list删除是O(n)的操作，会很费时。
        s = deque(s)
        res = self.traversal(s)

        return res


s = Solution()
print(s.calculate(s="2*(5+5*2)/3+(6/2+8)"))
