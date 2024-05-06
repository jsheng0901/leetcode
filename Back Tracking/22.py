from typing import List


class Solution1:
    def __init__(self):
        self.result = []
        self.path = []

    def is_valid(self):
        # 指针check是否是合理的string
        balance = 0
        for i in self.path:
            if i == "(":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

        return balance == 0

    def backtracking(self, n, index):
        # 走到最后组合
        if index == n * 2:
            # check是否合理的组合string
            if self.is_valid():
                # 记录进结果
                self.result.append("".join(self.path))
            return

        # 回溯找到所有组合
        for i in ["(", ")"]:
            self.path.append(i)
            self.backtracking(n, index + 1)
            self.path.pop()

        return

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time O(2^(2n) * n)  每个位置两种选择，总共2n个长度，每次放置都需要O(n)的操作
        Space O(2^(2n) * n)
        找到所有组合情况，每次check组合是不是合理的string，是的话加入结果，不是的话结束递归。
        """
        self.backtracking(n, 0)

        return self.result


class Solution2:
    def __init__(self):
        self.result = []
        self.path = []

    def backtracking(self, n, index, num_open, num_close):
        # 当放完所有指针的时候，说明找到一个合理的组合，记录进结果
        if index == n * 2:
            self.result.append("".join(self.path))
            return

        # 如果开括号大于等于闭括号，才是合理的组合，如果小于不可能是合理的组合
        if num_open >= num_close:
            # 如果开括号少于n，此时有两种选择
            if num_open < n:
                # 继续放置开括号
                self.path.append("(")
                # 记录括号个数
                self.backtracking(n, index + 1, num_open + 1, num_close)
                # 回溯弹出之前加入情况
                self.path.pop()

                # 放置闭括号
                self.path.append(")")
                # 记录括号个数
                self.backtracking(n, index + 1, num_open, num_close + 1)
                # 回溯弹出之前加入情况
                self.path.pop()
            # 如果开括号大于n，此时只有一种选择
            else:
                # 放置闭括号
                self.path.append(")")
                # 记录括号个数
                self.backtracking(n, index + 1, num_open, num_close + 1)
                # 回溯弹出之前加入情况
                self.path.pop()

        return

    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time O(4^n / sqrt(n)) 参考 https://leetcode.com/problems/generate-parentheses/editorial/
        Space O(n)
        典型的回溯题，这里可以用两个指针在构建的时候记录左右括号的个数，判断合理的指针个数情况来放置括号，并不需要尝试所有放置情况。
        详细见注释。
        """
        self.backtracking(n, 0, 0, 0)

        return self.result


s = Solution2()
print(s.generateParenthesis(n=3))
