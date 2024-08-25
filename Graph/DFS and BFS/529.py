from typing import List


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                           (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def get_nei_mines(self, board, i, j):
        m = len(board)
        n = len(board[0])
        number_mine = 0
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            if board[next_i][next_j] == "M":
                number_mine += 1

        return number_mine

    def dfs(self, board, i, j):
        m = len(board)
        n = len(board[0])

        # 如果点击是雷，标记雷，并结束递归
        if board[i][j] == "M":
            board[i][j] = "X"
            return
        # 如果是没有显示的空点
        if board[i][j] == "E":
            # 拿到附近八个方向的雷的数量
            number_mine = self.get_nei_mines(board, i, j)
            # 如果没有雷，则八个方向继续递归
            if number_mine == 0:
                board[i][j] = "B"
                for direction in self.directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    # 注意这里只有邻居也是空地没有翻过的点才递归
                    if board[next_i][next_j] == "E":
                        self.dfs(board, next_i, next_j)
            # 如果有雷，更新当前点的雷的个数，不递归邻居点
            elif number_mine > 0:
                board[i][j] = str(number_mine)

        return

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        Time O(m * n)
        Space O(n)
        非常直白的DFS逻辑，其实此题是扫雷游戏的解释，只需要按照解释翻译并更新当前节点的状态就行。详细见注释。
        """
        self.dfs(board, click[0], click[1])

        return board


s = Solution()
print(s.updateBoard(
    board=[["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]],
    click=[1, 2]))
print(s.updateBoard(
    board=[["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]],
    click=[3, 0]))
