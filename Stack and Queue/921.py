class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """记录有多少个不合规的括号留在最后的stack里面"""
        stack = []

        for i in range(len(s)):
            if len(stack) > 0 and s[i] == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)