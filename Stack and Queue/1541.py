class Solution1:
    def minInsertions(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        栈的思路，用res储存需要多少个右括号对应的插入操作，注意这里不是只插入右括号，是当右括号不合理的时候我们需要多少个插入操作来合理。
        栈里面存储的都是最终没有配对的左括号，每个左括号都需要2个右括号，最终相加得到结果。
        """

        # 初始化栈和
        res = 0
        stack = []
        i = 0

        while i < len(s):
            # 如果遇到左括号直接入栈
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                # 如果是右括号，如果栈内有元素
                if stack:
                    # 判断此括号的下一个括号，如果也是右括号说明是合理的组合
                    if i + 1 < len(s) and s[i + 1] == ")":
                        # 入栈的左括号弹出
                        stack.pop()
                        # 注意这里一定要跳两步，因为下一个已经是合理的右括号并检查过
                        i += 2
                    else:
                        # 如果下一个不是右括号或者走到底了，说明此时需要插入一个右括号
                        stack.pop()
                        # 左括号已经合理，因为插入了一个右括号
                        res += 1
                        # 向下移动一位
                        i += 1
                else:
                    # 如果是空栈，同理检查下一个是不是右括号，如果是则说明需要插入一个左括号，
                    # 注意这里res记录的是插入的操作顺序不是只有右括号的插入数量
                    if i + 1 < len(s) and s[i + 1] == ")":
                        res += 1
                        # 同理跳两步
                        i += 2
                    # 如果下一个不是右括号或者走到底了，需要插入一个右括号一个左括号，及两此插入
                    else:
                        res += 2
                        # 跳一步
                        i += 1
        # 总共插入的次数加上栈里面剩下的左括号的数量 * 2，及总共需要的次数
        return res + 2 * len(stack)


class Solution2:
    def minInsertions(self, s: str) -> int:
        """
        Time O(n)
        Space O(1)
        不用栈，用一个变量need记录对应右括号的需求个数。res记录插入次数。详细见注释。
        """
        # 记录需要多少次插入
        res = 0
        # 记录需右括号的需求量
        need = 0
        for i in range(len(s)):
            # 当遇到左括号的时候
            if s[i] == '(':
                # 一个左括号对应两个右括号
                need += 2
                # 当遇到左括号时，若对右括号的需求量为奇数，需要插入 1 个右括号。因为一个左括号需要两个右括号，右括号的需求必须是偶数
                if need % 2 == 1:
                    # 插入一个右括号
                    res += 1
                    # 对右括号的需求减一
                    need -= 1
            elif s[i] == ')':
                need -= 1
                # 当 need == -1 时，意味着我们遇到一个多余的右括号，显然需要插入一个左括号
                if need == -1:
                    # 需要插入一个左括号
                    res += 1
                    # 由于一个左括号需要两个右括号，所以对右括号的需求量变为 1，因已经遇到了一个，只需要再加一个即可
                    need = 1
        # 这里最终返回两个值的和，因为res记录的是插入的次数，need记录的是对右括号的需求，如果最后不为0说明还有多余的
        return res + need


s = Solution2()
print(s.minInsertions(s="))())("))
