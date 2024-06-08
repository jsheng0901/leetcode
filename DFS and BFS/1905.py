from typing import List


class Solution:
    def __init__(self):
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(self, grid, i, j):
        # 不用写递归判断，因为进入递归的数据都是在loop里面判断过的
        m = len(grid)
        n = len(grid[0])

        # 改变岛屿变成海洋
        grid[i][j] = 0

        for d in self.dirs:
            next_i = i + d[0]
            next_j = j + d[1]
            # 越界
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            # 访问过或者是海洋
            if grid[next_i][next_j] == 0:
                continue
            # 进入dfs的数据都是合理的下一个坐标
            self.dfs(grid, next_i, next_j)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(1)
        这道题的关键在于，如何快速判断子岛屿，当岛屿 B 中所有陆地在岛屿 A 中也是陆地的时候，岛屿 B 是岛屿 A 的子岛。
        反过来说，如果岛屿 B 中存在一片陆地，在岛屿 A 的对应位置是海水，那么岛屿 B 就不是岛屿 A 的子岛。
        那么，我们只要遍历 grid2 中的所有岛屿，把那些不可能是子岛的岛屿排除掉，剩下的就是子岛。
        """
        m, n = len(grid1), len(grid1[0])

        # 遍历 grid2，将非子岛的岛屿淹掉
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i, j)

        # 现在 grid2 中剩下的岛屿都是子岛，计算岛屿数量
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    self.dfs(grid2, i, j)

        return res


s = Solution()
print(s.countSubIslands(grid1=[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                        grid2=[[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]))
print(s.countSubIslands(grid1=[[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                        grid2=[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))
