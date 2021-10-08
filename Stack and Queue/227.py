class Solution:
    def calculate(self, s: str) -> int:
        """
        从左到右遍历 s
        如果是数字，则更新数字
        如果是空格，则跳过
        如果是运算符，则按照运算符规则计算，并将计算结果重新入栈
        """
        stack = []
        pre_operation = '+'
        num = 0
        s += '+'
        # 最后需要一个运算符，来计算最后个pre_peration的运算，其实每一次loop到运算符号时候，是计算前一个运算符号的计算
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


s = Solution()
print(s.calculate('1+2*3'))