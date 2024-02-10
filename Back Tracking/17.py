class Solution:
    def __init__(self):
        self.letter_mapping = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                               7: "pqrs", 8: "tuv", 9: "wxyz"}
        self.result = []
        self.string = ''

    def backtracking(self, digits, index):
        """
        先找出第一个数字对应字母，然后再递归进入下一个字母
        """
        # 这里处理的是下一个节点，所以index等于digits的长度及结束回溯
        if index == len(digits):
            self.result.append(self.string)
            return

        digit = int(digits[index])  # 将index指向的数字转为int
        letters = self.letter_mapping[digit]  # 取数字对应的字符集
        for i in range(len(letters)):
            self.string += letters[i]  # 处理
            self.backtracking(digits, index + 1)  # 递归，注意index+1，一下层要处理下一个数字了
            self.string = self.string[:len(self.string) - 1]  # 回溯

        return

    def letterCombinations(self, digits: str) -> [str]:
        """
        Time O(m^n * n) m -> max digits length in mapping   n -> digits length
        Space O(n)
        时间复杂度解释：总共有最长的digits长度乘以有多少个数字的组合，也就是m^n。对于每个组合需要一个O(n)。
        逻辑很直接，一个一个digits遍历，对于每个digits遍历他们的所有对应的组合。
        """
        if len(digits) == 0:
            return self.result

        self.backtracking(digits, 0)

        return self.result


s = Solution()
print(s.letterCombinations(digits="23"))
