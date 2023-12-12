class Solution1:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        栈的写法，遇到左括号入栈，右括号判断当前栈顶是数字还是左括号，如果是左括号说明score为1，如果是数字说明前面已经有合理的括号组合出现，
        此时会出现嵌套括号，比如(()) -> (1)，此时叠加前面全部的数字，直到遇到左括号，然后弹出左括号，叠加结果*2。最后sum栈则为结果。
        """
        stack = []

        for i in range(len(s)):
            char = s[i]
            # 左括号直接入栈
            if char == "(":
                stack.append(char)
            # 右括号
            else:
                # 栈顶是右括号，遇到合理组合 score为 1 入栈
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                # 栈顶是数字，遇到嵌套括号，叠加所有数字后 *2 入栈
                else:
                    tmp = 0
                    while stack[-1] != "(":
                        tmp += stack.pop()
                    stack.pop()
                    stack.append(2 * tmp)

        # 要sum整个stack，因为可能有全都是数字的情况
        return sum(stack)


class Solution2:
    def scoreOfParentheses(self, s):
        """
        Time O(n)
        Space O(n)
        同上的原理，但是左括号记为0分，遇到右括号，弹出然后直接 * 2，如果前面是左括号 * 0 则为0，此时 +1，如果不是0说明是嵌套括号，直接叠加
        """
        # 这里要配一个初始值代表当前分数方便更新当前分数
        stack = [0]

        for x in s:
            # 左括号直接为0
            if x == '(':
                stack.append(0)
            # 右括号
            else:
                # 弹出栈顶
                v = stack.pop()
                # 赋值给当前新的栈顶分数，*2 或者 1，取决于弹出的是 0 还是数字，弹出是0说明是连续括号，比如 ()()，
                # 弹出不是0说明是嵌套括号，比如 (())。
                stack[-1] += max(2 * v, 1)

        return stack.pop()


s = Solution2()
print(s.scoreOfParentheses(s="()()"))
print(s.scoreOfParentheses(s="(())"))
print(s.scoreOfParentheses(s="()"))
