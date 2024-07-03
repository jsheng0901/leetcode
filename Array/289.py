from typing import List


class Solution1:
    def gameOfLife(self, board: List[List[int]]) -> List:
        """
        Time O(m * n)
        Space O(m * n)
        此题最重要的就是理解题意，按照题目的意思直接implement就行，唯一难的地方是，因为是同时更新所有cell的状态，也就是说相邻的cell依赖
        原始的邻居cell的的值，这里可以直接copy一个原始值，计算有多少个live的邻居的时候用原始值计算即可，更新的时候用board。
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (rows > r >= 0) and (cols > c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1

        return board


class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> List:
        """
        Time O(m * n)
        Space O(1)
        一模一样的思路，区别在于我们直接在board上面改，对于原本是1但是改完应该是0的我们先赋值为-1，这样计算邻居的时候用绝对值来判断是不是1，
        这样就不会因为被改动过而影响其它的邻居cell计算live的邻居个数。对于原本是0但是改完应该是1的cell，我们赋值为2或者任意大于1的数，
        这样也不会影响原本的cell计算。
        对于follow up question，如果matrix是无限的情况参考 https://leetcode.com/problems/game-of-life/editorial/
        """
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    # row and column of the neighboring cell
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    if (rows > r >= 0) and (cols > c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 signifies the cell is now dead but originally was live.
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 signifies the cell is now live but was originally dead.
                    board[row][col] = 2

        # Get the final representation for the newly updated board.
        for row in range(rows):
            for col in range(cols):
                # 大于0的数需要变回1
                if board[row][col] > 0:
                    board[row][col] = 1
                # 小于0的数需要变回0
                else:
                    board[row][col] = 0

        return board


s = Solution2()
print(s.gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
