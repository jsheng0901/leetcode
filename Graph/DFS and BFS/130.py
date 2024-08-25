class Solution1:
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果数组长或宽小于等于2，则不需要替换
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        row, col = len(board), len(board[0])

        def dfs(i, j):
            """
            深度优先算法，如果符合条件，替换为A并进一步测试，否则停止
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'A'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 从外围开始
        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)

        for j in range(col):
            dfs(0, j)
            dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

        return board


class Solution2:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(self, board, i, j):
        """
        DFS一种写法，不用写递归判断，因为进入递归的数据都是在loop里面判断过的
        """
        m = len(board)
        n = len(board[0])

        board[i][j] = 'A'

        for d in self.dirs:
            next_i = i + d[0]
            next_j = j + d[1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            if board[next_i][next_j] == 'X' or board[next_i][next_j] == 'A':
                continue
            self.dfs(board, next_i, next_j)

    def solve(self, board: [[str]]) -> None:
        """
        Time O(m * n) 多次loop完整个board
        Space O(1) 没有额外空间，直接在board上面改
        DFS写法，与1020一模一样，区别在于这里需要记录的是中间是O的情况
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][n - 1] == 'O':
                self.dfs(board, i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[m - 1][j] == 'O':
                self.dfs(board, m - 1, j)

        # 最后不需要用DFS来判断更新O，直接loop整个board改动数据
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

        return board


s = Solution2()
print(s.solve(board=[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]))
