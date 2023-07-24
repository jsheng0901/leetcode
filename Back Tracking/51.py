import copy


class Solution:
    def __init__(self):
        # n 为输入的棋盘大小
        # row 是当前递归到棋牌的第几行了
        self.result = []
        self.chessboard_copy = []

    def is_valid(self, row, col, chessboard, n):
        # 检查列
        for i in range(row):    # 这是一个剪枝
            if chessboard[i][col] == 'Q':
                return False

        # 检查45度角是否有皇后
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 检查135度角是否有皇后
        r = row - 1
        c = col + 1
        while r >= 0 and c < n:
            if chessboard[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

    def backtracking(self, n, row, chessboard):
        if row == n:
            # self.chessboard_copy = copy.deepcopy(chessboard)   # 也可以在这做 copy, avoid 回溯 will change chessboard
            self.result.append(["".join(each) for each in self.chessboard_copy])
            return

        # 递归深度就是row控制棋盘的行，每一层里for循环的col控制棋盘的列，一行一列
        for col in range(n):
            if self.is_valid(row, col, chessboard, n):
                chessboard[row][col] = 'Q'
                self.chessboard_copy = copy.deepcopy(chessboard)   # make a copy avoid 回溯 will change chessboard
                self.backtracking(n, row + 1, chessboard)
                chessboard[row][col] = '.'          # 回溯，撤销皇后

    def solveNQueens(self, n: int) -> [[str]]:
        # 因为chessboard的大小和n有关系，所以没办法变成全局变量，只能作为参数往下传
        # 必须放入n个皇后，所以n = 2, 3都没有结果
        chessboard = [['.'] * n for i in range(n)]

        self.backtracking(n, 0, chessboard)

        return self.result


s = Solution()
print(s.solveNQueens(n=1))
