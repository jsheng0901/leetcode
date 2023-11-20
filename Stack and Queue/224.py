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
        同上227对于没有括号的逻辑，区别在于当我们遇到括号的时候也就是当前节点是括号的时候，我们就可以开始递归了，遇到当前节点是反括号的时候，
        说明此时括号内的结算结束了，可以结束当前递归了，返回括号内的数字和并通过符号判断入栈。把string转化成双向列队，
        每次从左到右列队的开始pop出来处理当前节点字符。
        括号带有天然的递归优势，因为递归开始和结束的信号很明显。
        """
        # 小细节这里要用双向列队保证后面弹出左边是O(1)的操作不然普通的list删除是O(n)的操作，会很费时。
        s = deque(s)
        res = self.traversal(s)

        return res


s = Solution()
print(s.calculate(s="(1+(4+5+2)-3)+(6+8)"))
