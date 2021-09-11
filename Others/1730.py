from collections import deque


class Solution:
    def getFood(self, grid: [[str]]) -> int:
        """ O(n*m) time, O(n*m) space, worst case go through all points """
        # this is a typical BFS question, each time we try all the possible dirs by adding it to queue
        # iterate the element in curr level, add all next levels into the queue
        # the first time we met a food will be the shorted length by the nature of BFS
        # mark the visited sell so we don't need to go there again
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    queue.append([row, col])
                    break

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # bfs to check all the neighboring cells, use "V" to indicate this cell has been visited
        curr_step = 0
        while queue:
            curr_step += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for d in dirs:
                    next_row = row + d[0]
                    next_col = col + d[1]
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        if grid[next_row][next_col] == '#':
                            return curr_step
                        if grid[next_row][next_col] == 'O':
                            grid[next_row][next_col] = 'V'
                            queue.append([next_row, next_col])
        return -1


s = Solution()
print(s.getFood(grid=[["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"], ["X", "O", "O", "#", "O", "X"],
                      ["X", "X", "X", "X", "X", "X"]]))
