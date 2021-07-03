class Solution:
    def __init__(self):
        self.letter_mapping = { 0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                                7: "pqrs", 8: "tuv", 9: "wxyz"}
        self.result = []
        self.string = ''

    def backtracking(self,digits, index):
        """
        先找出第一个数字对应字母
        :param digits:
        :param index:
        :return:
        """
        if index == len(digits):
            self.result.append(self.string)
            return

        digit = int(digits[index])      # 将index指向的数字转为int
        letters = self.letter_mapping[digit]    # 取数字对应的字符集
        for i in range(len(letters)):
            self.string += letters[i]       # 处理
            self.backtracking(digits, index + 1)    # 递归，注意index+1，一下层要处理下一个数字了
            self.string = self.string[:len(self.string) - 1]    # 回溯

    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0:
            return self.result

        self.backtracking(digits, 0)

        return self.result
