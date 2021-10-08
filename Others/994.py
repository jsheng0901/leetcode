class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        """
        O(n) time, O(n) space, n is size of grid
        bfs, 记录所有2先，然后对每个2同时做bfs找到可以去到的所有是1的情况的点并记录进queue，和seen list，记录去过的点
        防止重复loop，最后判断可以去到的为1的点和原本为2的点和0的点的总和，等于Grid size则说明可以感染完，并return steps
        """
        seen = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        self.steps = -1

        def bfs(queue, grid, seen):

            while queue:
                size = len(queue)
                self.steps += 1
                for i in range(size):
                    cur_i, cur_j = queue.pop(0)

                    for d in directions:
                        new_i, new_j = cur_i + d[0], cur_j + d[1]
                        if (new_i, new_j) not in seen:
                            if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                                seen.append((new_i, new_j))
                                queue.append((new_i, new_j))
            return

        empty_number = 0
        one_number = 0
        two_number = 0
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    two_number += 1
                    queue.append((i,j))

                if grid[i][j] == 0:
                    empty_number += 1

                if grid[i][j] == 1:
                    one_number += 1

        bfs(queue, grid, seen)

        if empty_number == rows * cols:
            return 0
        elif one_number == rows * cols:
            return -1
        elif two_number + empty_number == rows * cols:
            return 0
        elif empty_number + len(seen) + two_number == rows * cols:
            return self.steps
        else:
            return -1


s = Solution()
# print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
# print(s.orangesRotting(grid=[[0, 2, 2]]))