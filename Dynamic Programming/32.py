class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        """
        Time O(2 * n)
        Spce O(n)
        定义：dp[i] 表示以 i - 1 结尾的s的最长连续符合条件的括号子串。
        那么不合理的一定是0，合理的当前位置由前一个位置的括号 +2，这里只用到了临近括号的信息。需要先记录一下不合理的括号额位置。
        遇到不合理的则直接为0，合理但是没有配对的等于前一个位置的dp信息，及dp[i] = dp[i - 1]，合理并且配对的则dp[i] +2。
        此方法要loop两次，更耗时。
        """
        # 记录合理的index
        stack = []
        # 记录最终结果
        result = float('-inf')
        dp = [0] * (len(s) + 1)
        # 记录不合理的index
        invalid_stack = []
        # 记录所有不合理的左括号的 index
        for i in range(len(s)):
            cur = s[i]
            if cur == "(":
                invalid_stack.append(i)
            else:
                if invalid_stack:
                    top = s[invalid_stack[-1]]
                    if top == "(":
                        invalid_stack.pop()
                    else:
                        invalid_stack.append(i)
                else:
                    invalid_stack.append(i)

        # 再次loop一遍
        for i in range(1, len(dp)):
            cur = s[i - 1]
            # 如果是左括号，直接入栈
            if cur == "(":
                stack.append(cur)
                # 如果不是不合理的位置，说明是没有配对完的左括号，则长度等于前一个
                if i - 1 not in invalid_stack:
                    dp[i] = dp[i - 1]
            else:
                # 如果是右括号，并且栈内有合理左括号
                if stack:
                    # 弹出左括号
                    stack.pop()
                    # 当前长度等于前一个长度 +2
                    dp[i] = dp[i - 1] + 2
                    # 更新最长距离
                    result = max(result, dp[i])
                else:
                    # 如果右括号但是空栈并且不是不合理的右括号，则长度等于前一个
                    # 如果是不合理右括号，直接为0也就是初始值，所以不需要赋值这里
                    if i - 1 not in invalid_stack:
                        dp[i] = dp[i - 1]

        # 检查结果，如果都是不合理的括号，则为0
        return 0 if result == float('-inf') else result


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        """
        Time O(n)
        Space O(n)
        定义：dp[i] 表示以 i - 1 结尾的s的最长符合条件的括号子串。并不需要连续这个定义，说明可以是前好几个位置的，并不要只考虑临近的位置。
        栈内记录的是合理的左括号的index，这样如果我们遇到了连续的合理的括号组合，可以用栈内的index和当前index找出此时最长长度，
        如果是不合理的结尾子串，则直接为0，用dp数组记录下来。
        ex: "()(" 当我们loop到最后一个左括号我们不用担心后面有没有配对的右括号，根据dp的定义此时以最后一个左括号结尾的子串一定是0，
        因为是不合理的配对，如果此左括号后还有配对成功的右括号，我们在栈内会记录下来此时左括号的index，之后有右括号，则相减登出长度。
        """
        # 特殊情况，空string
        if len(s) == 0:
            return 0
        # 记录合理的左括号 index
        stack = []
        # 记录最终结果
        result = float('-inf')
        # dp[i] 的定义：记录以 s[i-1] 结尾的最长合法括号子串长度
        dp = [0] * (len(s) + 1)

        for i in range(len(s)):
            cur = s[i]
            # 遇到左括号，记录索引
            if cur == "(":
                stack.append(i)
                # 左括号不可能是合法括号子串的结尾
                dp[i + 1] = 0
            else:
                # 遇到右括号，且栈不为空
                if stack:
                    # 配对的左括号对应索引
                    top = stack.pop()
                    # 以这个右括号结尾的最长子串长度
                    dp[i + 1] = 1 + i - top + dp[top]
                    # 更新最长长度，注意这里dp的index都要 +1 根据定义
                    result = max(result, dp[i + 1])
                # 遇到右括号，且栈为空
                else:
                    # 没有配对的左括号
                    dp[i + 1] = 0

        # 检查结果，如果都是不合理的括号，则为0
        return 0 if result == float('-inf') else result


s = Solution1()
print(s.longestValidParentheses(s="())"))
print(s.longestValidParentheses(s=")()())()()("))
print(s.longestValidParentheses(s="("))
