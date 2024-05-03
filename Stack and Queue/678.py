class Solution1:
    def dp(self, index, open_count, s, memo):
        # If reached end of the string, check if all brackets are balanced
        if index == len(s):
            return open_count == 0

        # If already computed, return memoized result
        if memo[index][open_count] != -1:
            return memo[index][open_count]

        # 初始化当前节点子节点返回情况
        is_valid = False

        # If encountering '*', try all three possibilities
        if s[index] == "*":
            # Treat '*' as '('
            is_valid = is_valid or self.dp(index + 1, open_count + 1, s, memo)

            # Treat '*' as ')'
            if open_count > 0:
                is_valid = is_valid or self.dp(index + 1, open_count - 1, s, memo)

            # Treat '*' as empty
            is_valid = is_valid or self.dp(index + 1, open_count, s, memo)
        # Handle '(' and ')'
        else:
            # Increment count for '('
            if s[index] == "(":
                is_valid = is_valid or self.dp(index + 1, open_count + 1, s, memo)
            # Decrement count for ')'
            elif open_count > 0:
                is_valid = is_valid or self.dp(index + 1, open_count - 1, s, memo)

        # Memoize and return the result
        memo[index][open_count] = is_valid

        return is_valid

    def checkValidString(self, s: str) -> bool:
        """
        Time O(n^2)
        Space O(n^2)
        很简单的思路，对于所有星号的字符，我们尝试所有情况，如果走到最后，所有开括号都被消除了说明是一条valid的path，则返回true，所有路径中
        只需要知道其中一条即可，用备忘录记录走过的情况。每次记录走到的index和当时的开括号的个数代表状态。详细见注释。
        """
        n = len(s)
        # 备忘录，构建一个足够大的备忘录，开括号的个数最多为全都是开括号也是就n个
        memo = [[-1] * n for _ in range(n)]

        return self.dp(0, 0, s, memo)


class Solution2:

    def checkValidString(self, s: str) -> bool:
        """
        Time O(n)
        Space O(n)
        不需要遍历所有组合情况，可以用两个stack记录所有的开括号和所有的星号，如果遇到闭括号先查看是否有开括号匹配，如果有直接配对，如果没有
        查看星号是否有，有的话也直接匹配，如果都没有说明是多余的闭括号，直接返回false。这里还需要进一步check所有闭括号匹配完后的情况。
        可能出现多余的开括号和星号，如果当前最后一个开括号大于星号，说明不可能有匹配的闭括号出现，直接返回false，
        最后check是否所有开括号都匹配完。
        """
        # Stacks to store indices of open brackets and asterisks
        stack_open = []
        stack_star = []

        for idx, val in enumerate(s):
            # If current character is an open bracket, push its index onto the stack
            if val == "(":
                stack_open.append(idx)
            # If current character is an asterisk, push its index onto the stack
            elif val == "*":
                stack_star.append(idx)
            # current character is a closing bracket ')'
            else:
                # If there are open brackets available, use them to balance the closing bracket
                if stack_open:
                    stack_open.pop()
                # If no open brackets are available, use an asterisk to balance the closing bracket
                elif stack_star:
                    stack_star.pop()
                # unmatched ')' and no '*' to balance it.
                else:
                    return False

        # Check if there are remaining open brackets and asterisks that can balance them
        while stack_open and stack_star:
            # If an open bracket appears after an asterisk, it cannot be balanced, return false
            if stack_open.pop() > stack_star.pop():
                return False

        # If all open brackets are matched and there are no unmatched open brackets left, return true
        return len(stack_open) == 0


class Solution3:
    def checkValidString(self, s: str) -> bool:
        """
        Time O(n)
        Space O(1)
        思路同2116，把星号当做万能符合即可，记录左右括号的个数是否balance，两次遍历check。
        """
        balance = 0

        for i in range(len(s)):
            # 如果是开括号或者是星号 +1
            if s[i] == "(" or s[i] == "*":
                balance += 1
            else:
                balance -= 1
            # 不合规直接返回 false
            if balance < 0:
                return False

        balance = 0

        for i in range(len(s) - 1, -1, -1):
            # 如果是闭括号或者是星号 +1
            if s[i] == ")" or s[i] == "*":
                balance += 1
            else:
                balance -= 1
            # 不合规直接返回 false
            if balance < 0:
                return False

        return True


class Solution4:

    def checkValidString(self, s: str) -> bool:
        """
        Time O(n)
        Space O(1)
        同思路3，只是双向遍历同时进行在一个loop里面写法。
        """
        open_count = 0
        close_count = 0
        length = len(s) - 1

        # Traverse the string from both ends simultaneously
        for i in range(length + 1):

            # 从左向右
            # Count open parentheses or asterisks
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1

            # 从右向左
            # Count close parentheses or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1

            # If at any point open count or close count goes negative, the string is invalid
            if open_count < 0 or close_count < 0:
                return False

        # If open count and close count are both non-negative, the string is valid
        return True


s = Solution4()
print(s.checkValidString(s="(*))"))
print(s.checkValidString(s="(*)"))
