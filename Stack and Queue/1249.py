class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Time O(n)
        Space O(n)
        当遇到不是 ( 时候并且stack为空的时候，就说明遇到了要移除的 ）符号，这里最巧妙的是记录index而不是符号本身
        多余的（ 符号会记录在最终的stack里面，这些都是要被移除的符号。最终union起来两个需要被移除的括号的index，再loop一遍整个string，
        不在需要被移除的set里面的加入最终答案。
        """
        index_to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            elif len(stack) == 0:
                index_to_remove.add(i)
            else:
                stack.pop()

        index_to_remove = index_to_remove.union(set(stack))

        result = []
        for i, c in enumerate(s):
            if i not in index_to_remove:
                result.append(c)

        return "".join(result)


class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Time O(n)
        Space O(n)
        同样的逻辑，不同的判断方式
        """
        # 初始化为set方面后续查存在保证查找为O(1)
        stack = set()
        index_to_remove = set()

        for i in range(len(s)):
            # 当前字符串
            c = s[i]
            # 如果是字母，则跳过
            if c.isalpha():
                continue
            # 如果是括号开始判断
            else:
                # 左括号直接入栈，这里入的是index
                if c == "(":
                    stack.add(i)
                # 如果右括号，开始判断
                else:
                    # 如果栈内有元素，说明右配对成功的，弹出栈顶左括号
                    if stack:
                        stack.pop()
                    # 如果没有元素，说明是需要被移除的右括号，记录进set
                    else:
                        index_to_remove.add(i)

        # union两个set为一个需要被移除的set
        index_to_remove = index_to_remove.union(stack)
        # 再过一次字符串s，不需要被移除的加入进结果，这里用set查存更快
        res = ""
        for i in range(len(s)):
            if i not in index_to_remove:
                res += s[i]

        return res


s = Solution2()
print(s.minRemoveToMakeValid(s="lee(t(c)o)de)"))
