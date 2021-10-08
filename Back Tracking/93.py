class Solution1:
    def __init__(self):
        self.result = []  # 存放组合集合
        self.path = []  # 符合条件的组合

    def isValid(self, s, start, end):
        if start > end:
            return False

        sub = s[start: end]

        if len(sub) == 0:
            return False

        if sub[0] == '0' and len(sub) > 1:    # 0开头的数字不合法
            return False

        for i in sub:
            if i > '9' or i < '0':     # 遇到非数字字符不合法
                return False

        if float(sub) > 255:
            return False

        return True

    def backtracking(self, s, start_index, point_num):
        if point_num == 3:  # 逗点数量为3时，分隔结束
            # 判断第四段子字符串是否合法，如果合法就放进result中
            if self.isValid(s, start_index, len(s)):
                self.result.append(s)
            return

        for i in range(start_index, len(s)):
            # sub = s[start_index: i + 1]
            if self.isValid(s, start_index, i + 1):  # 判断合理性
                s = s[: i + 1] + '.' + s[i + 1:]
                point_num += 1                              # 在i的后面插入一个逗点
                self.backtracking(s, i + 2, point_num)      # 插入逗点之后下一个子串的起始位置为i+2
                point_num -= 1
                s = s[: i + 1] + s[i + 2:]                  # 回溯删掉逗点
            else:
                break                                       # 不合法，直接结束本层循环

    def restoreIpAddresses(self, s: str) -> [str]:
        """
        切割等同于组合，每次切割完判断合不合理，然后添加再继续递归，此题最重要的是回溯的过程要正确的找到之前的切割点
        """

        self.backtracking(s, 0, 0)

        return self.result


class Solution2:
    def __init__(self):
        self.result = []
        self.path = []

    def isValid(self, s, start, end):
        if start > end:
            return False

        sub = s[start: end]

        if len(sub) == 0:
            return False

        if sub[0] == '0' and len(sub) > 1:  # 0开头的数字不合法
            return False

        for i in sub:
            if i > '9' or i < '0':  # 遇到非数字字符不合法
                return False

        if float(sub) > 255:
            return False

        return True

    def backtracking(self, s, start_index, point_number):
        if point_number == 3:
            if self.isValid(s, start_index, len(s)):
                # self.result.append(s)
                self.path.append(s[start_index: len(s)])
                self.result.append(".".join(self.path))
                self.path = self.path[:-1]
            return

        for i in range(start_index, start_index + 3):       # 优化一个loop，可以没必要进valid
            if self.isValid(s, start_index, i + 1):
                self.path.append(s[start_index: i + 1])
                point_number += 1
                self.backtracking(s, i + 1, point_number)
                self.path = self.path[:-1]
                point_number -= 1
            else:                                           # 如果不符合就break，没必要继续展开tree
                break

        return

    def restoreIpAddresses(self, s: str) -> [str]:
        """一样的逻辑只是加入string的方式不同，这样更容易理解一点，但是要注意两次回溯"""
        self.backtracking(s, 0, 0)

        return self.result


s = Solution1()
print(s.restoreIpAddresses(s="010010"))
