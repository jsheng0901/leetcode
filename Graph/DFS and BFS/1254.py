from typing import List


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(self, grid, i, j):
        # 标准DSF遍历2-D matrix的写法
        m, n = len(grid), len(grid[0])

        grid[i][j] = 1
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 越界跳过
            if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                continue
            # 之前走过，跳过
            if grid[next_i][next_j] == 1:
                continue
            # 遍历下一个点
            self.dfs(grid, next_i, next_j)

        return

    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(1)
        对于所有岛屿，如果有一个岛屿和边界相邻说明此岛屿一定不能被水完全包围，所以我们只需要把所有和边界相接壤的岛屿填起来，
        然后再直接找有多少个岛屿就是最终答案。这里不用额外空间，直接填岛屿为陆地。
        """
        m, n = len(grid), len(grid[0])
        # 填满边界岛屿
        for j in range(n):
            # 注意这里一定要判断一下是不是岛屿先，不然如果是陆地也直接填的话会把所有岛屿都填完了
            # 把靠上边的岛屿淹掉
            if grid[0][j] == 0:
                self.dfs(grid, 0, j)
            # 把靠下边的岛屿淹掉
            if grid[m - 1][j] == 0:
                self.dfs(grid, m - 1, j)

        for i in range(m):
            # 把靠左边的岛屿淹掉
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            # 把靠右边的岛屿淹掉
            if grid[i][n - 1] == 0:
                self.dfs(grid, i, n - 1)

        # 遍历 grid，剩下的岛屿都是封闭岛屿
        res = 0
        for i in range(m):
            for j in range(n):
                # 同第200题，直接遍历所有岛屿，并标记
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)

        return res


s = Solution()
print(s.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
print(s.closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
