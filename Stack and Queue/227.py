class Solution1:
    def calculate(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        从左到右遍历 s
        如果是数字，则更新数字，如果是空格，则跳过，如果是运算符，则按照运算符规则计算，并将计算结果重新入栈，
        这里遇到符号的时候是更新前一个符号和数字的结果。
        """
        stack = []
        pre_operation = '+'
        num = 0
        s += '+'
        # 最后需要一个运算符，来计算最后个pre_operation的运算，其实每一次loop到运算符号时候，是计算前一个运算符号的计算
        # 再更新目前这个运算符号，所以最后一个运算符号，必须要一个不用参与运算的+号来激发前一个及最后一个真正需要运算的运算符

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)     # 如果是数字则持续更新目前的数字
            elif c == ' ':
                continue
            else:
                if pre_operation == '+':        # 前一个运算符的运算
                    stack.append(num)
                elif pre_operation == '-':
                    stack.append(-num)
                elif pre_operation == '*':
                    stack.append(stack.pop() * num)
                elif pre_operation == '/':
                    stack.append(int(stack.pop() / num))
                pre_operation = c       # 更新运算符记录
                num = 0                 # 重置数字大小

        return sum(stack)


class Solution2:
    def calculate(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        同上逻辑，区别在于我们在前面加一个 + 的运算符合来更新初始结果，最后一个的时候我们判断一下是不是走到底了，
        走到最后以一个了就直接进运算符号开始计算。
        """
        s = "+" + s
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + (int(ord(c)) - int(ord("0")))

            if (c.isdigit() is False and c != " ") or i == len(s) - 1:
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

        return sum(stack)


s = Solution2()
print(s.calculate('1+2*3'))
