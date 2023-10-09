class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        记录有多少个不合规的括号留在最后的stack里面
        """
        stack = []

        for i in range(len(s)):
            # 如果栈非空，并且top元素可以和当前元素匹配，则找到一对合规的括号，弹出栈，这也是唯一合规的组合
            if stack and s[i] == ')' and stack[-1] == '(':
                stack.pop()
            # 其它情况都入栈
            else:
                stack.append(s[i])

        # 最终有多少留在栈内的元素就是需要insert的最小个数
        return len(stack)


s = Solution()
print(s.minAddToMakeValid(s="())"))
