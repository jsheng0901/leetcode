class Solution:
    def __init__(self):
        self.res = 0

    def is_valid(self, row, col, chessboard, n):
        # 检查列
        for i in range(row):  # 这是一个剪枝
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
            self.res += 1
            return

        for col in range(n):
            if self.is_valid(row, col, chessboard, n):
                chessboard[row][col] = 'Q'
                self.backtracking(n, row + 1, chessboard)
                chessboard[row][col] = '.'

        return

    def totalNQueens(self, n: int) -> int:
        """
        Time O(n! * n)
        Space O(n)
        同51一模一样的解法，只是每次找到合理的棋盘的时候全局变量 +1
        """
        chessboard = [['.'] * n for i in range(n)]

        self.backtracking(n, 0, chessboard)

        return self.res


s = Solution()
print(s.totalNQueens(n=4))
