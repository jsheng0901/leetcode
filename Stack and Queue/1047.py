class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Time O(n) same as 20
        Space O(n)
        如果栈顶元素等于当前元素说明遇到重复的元素了，直接弹出，如果不相等直接入栈。
        """
        stack = []
        for i in s:
            # 栈顶等于当前元素，及遇到了重复元素
            if stack or stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()

        # 构建剩下的字符串变成string，不用list.join()       return ''.join(stack)
        result = ''
        while len(stack) > 0:
            result += stack.pop()

        # 反转string, 因为stack pop出来的顺序是反的，或者直接弹出的时候从栈底弹出，虽然这样可以通过list做到但是不符合stack的定义
        return result[::-1]


s = Solution()
print(s.removeDuplicates('abbaca'))

