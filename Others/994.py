from typing import List


class Solution:
    def __init__(self):
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(self, queue, seen, grid):
        m = len(grid)
        n = len(grid[0])
        # 注意这里起始为 -1
        step = -1

        while queue:
            size = len(queue)
            for i in range(size):
                cur_i, cur_j = queue.pop(0)

                for d in self.directions:
                    next_i, next_j = cur_i + d[0], cur_j + d[1]
                    # 越界，跳过
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    # 访问过，跳过
                    if (next_i, next_j) in seen:
                        continue
                    # 一定要保证下一个是新鲜橘子，如果不是跳过
                    if grid[next_i][next_j] != 1:
                        continue

                    # 进列队，并记录访问过
                    seen.add((next_i, next_j))
                    queue.append((next_i, next_j))

            # 步骤 +1，结束一层遍历
            step += 1

        return step

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        典型的BFS找最短路径的题型， 记录所有2先，然后对每个2同时做BFS找到可以去到的所有是1的情况的点并记录进queue，
        和seen list，记录去过的点，防止重复loop，最后判断可以去到的为1的点和原本为2的点和0的点的总和，
        等于Grid size则说明可以感染完，并返回最短路径也就是时间。
        """
        # 用set来记录访问过的记录，加入查存在，并且可以达到记录访问个数
        seen = set()
        queue = []
        m = len(grid)
        n = len(grid[0])
        # 记录每种情况的个数
        empty_number = 0
        one_number = 0
        two_number = 0

        for i in range(m):
            for j in range(n):
                # 如果是烂橘子
                if grid[i][j] == 2:
                    two_number += 1
                    # 进列队，注意这里不需要进seen，因为我们已经记录了为2的个数
                    queue.append((i, j))
                # 如果是空cell
                if grid[i][j] == 0:
                    empty_number += 1
                # 如果是新鲜橘子
                if grid[i][j] == 1:
                    one_number += 1

        # BFS找最短时间访问完所有新鲜橘子
        min_step = self.bfs(queue, seen, grid)

        # 如果都是空cell，返回0
        if empty_number == m * n:
            return 0
        # 如果都是新鲜橘子，没有烂橘子，返回 -1 不可能感染到
        elif one_number == m * n:
            return -1
        # 如果只有空cell和新鲜橘子，返回0
        elif two_number + empty_number == m * n:
            return 0
        # 如果三种情况加起来更好是所有cell个数，找到一个可能性，返回最短时间
        elif empty_number + len(seen) + two_number == m * n:
            return min_step
        # 其它情况都是 -1
        else:
            return -1


s = Solution()
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
print(s.orangesRotting(grid=[[0, 2, 2]]))
