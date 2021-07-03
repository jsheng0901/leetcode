class Solution:
    def __init__(self):
        self.result = []  # 存放组合集合
        self.path = []  # 符合条件的组合

    def isPalindrome(self, sub):
        start = 0
        end = len(sub) - 1
        for i in range(len(sub)):
            if sub[start] != sub[end]:
                return False

            start += 1
            end -= 1
        return True

    def backtracking(self, s, start_index):
        # 如果起始位置已经大于s的大小，说明已经找到了一组分割方案了
        if start_index >= len(s):
            self.result.append(self.path)
            return

        for i in range(start_index, len(s)):
            sub = s[start_index: i + 1]
            if self.isPalindrome(sub):  # 是回文子串
                self.path.append(sub)
            else:
                continue

            self.backtracking(s, i + 1)
            self.path = self.path[:len(self.path) - 1]

    def partition(self, s: str) -> [[str]]:
        """
        切割等同于组合，每次切割完判断是不是回文，然后添加再继续递归
        """

        self.backtracking(s, 0)

        return self.result


s = Solution()
print(s.partition(s="aab"))
