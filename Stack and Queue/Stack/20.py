class Solution1:
    def isValid(self, s: str) -> bool:
        """
        Time O(n)
        Space O(n)
        用栈的逻辑来记录括号pair是否合理
        """
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif len(stack) == 0 or stack[-1] != i:
                # 第一种情况，右括号有没有匹配的左括号，第二种情况加进来的用括号和左括号不匹配
                return False
            else:
                stack.pop()
        return len(stack) == 0    # 第三种情况，左括号还有没有匹配完的右括号


class Solution2:
    def isValid(self, s: str) -> bool:
        """
        Time O(n)
        Space O(n)
        用栈的逻辑来记录括号pair是否合理，同思路1，换个同一的写法。
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i not in mapping:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top != mapping[i]:
                        return False
        return len(stack) == 0


s = Solution2()
print(s.isValid('{{{}}}'))
