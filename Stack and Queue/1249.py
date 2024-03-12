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


class Solution3:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Time O(n)
        Space O(n)

        """
        # Pass 1: Remove all invalid ")"
        first_pass_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(c)

        # Pass 2: Remove the rightmost "("
        result = []
        # 记录有多少个左括号需要被保留下来
        open_to_keep = open_seen - balance
        for c in first_pass_chars:
            if c == "(":
                open_to_keep -= 1
                # 如果需要保留的左括号已经全部用完为负数，也就是说多出来的不需要保留，直接跳过
                if open_to_keep < 0:
                    continue
            result.append(c)

        return "".join(result)


class Solution4:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Time O(n)
        Space O(1)
        如果输出不算空间的话，我们只需要噪输出结果上进行删除不合理的括号，从左往右删除不合理的右括号，从后往前删除不合理的左括号。
        """
        left = 0
        s = list(s)
        # 删除右括号
        for i, c in enumerate(s):
            if c == '(':
                left += 1
            elif c == ')':
                if not left:
                    s[i] = ""
                else:
                    left -= 1
        # 删除左括号
        for i in range(len(s) - 1, -1, -1):
            if not left:
                break
            if s[i] == '(':
                s[i] = ""
                left -= 1

        return "".join(s)


s = Solution3()
print(s.minRemoveToMakeValid(s="lee(((t(c)o)de)"))
