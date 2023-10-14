from typing import List


class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(self, board, visited, i, j):
        # DFS标准模版，永远处理当前节点，进递归的都是提前判断过合理的节点
        m = len(board)
        n = len(board[0])

        # 每次记录当前节点访问过
        visited[i][j] = True
        # 开始四个方向遍历
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 越界，则不合理，跳过
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            # 不是战船，则跳过
            if board[next_i][next_j] == ".":
                continue
            # 访问过的战船，则跳过
            if visited[next_i][next_j] is True:
                continue
            # 符合条件的下一个节点，进入递归
            self.dfs(board, visited, next_i, next_j)

        return

    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        DFS模板题，遇到战船就开始四个方向遍历，把都是战船的标记起来，走出DFS后说明找到了一搜战船，计数器 +1，然后继续遍历棋盘。
        这里也可以不用visited数组记录是否访问过，直接在原始棋盘上改数值，如果访问过的战船就标记成比如 "B"，没访问过的还是 "X"。
        """
        m = len(board)
        n = len(board[0])

        # 初始化数组记录是否访问过
        visited = [[False] * n for _ in range(m)]
        num_ships = 0

        for i in range(m):
            for j in range(n):
                # 没访问过并且是战船，开始遍历
                if visited[i][j] is False and board[i][j] == "X":
                    num_ships += 1
                    self.dfs(board, visited, i, j)

        return num_ships


s = Solution()
print(s.countBattleships(board=[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
