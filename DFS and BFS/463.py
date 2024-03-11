from typing import List


class Solution:
    def __init__(self):
        self.perimeter = 0
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def dfs(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])

        # 标记访问过避免重复访问
        visited[i][j] = True

        # 遍历四个方向
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 如果是边界则周长 +1 并且跳过此方向
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                self.perimeter += 1
                continue
            # 如果是海洋则周长 +1 并且跳过此方向
            if grid[next_i][next_j] == 0:
                self.perimeter += 1
                continue
            # 如果访问过则跳过此方向，此时不需要周长 +1
            if visited[next_i][next_j]:
                continue
            # 遇到下一个岛屿陆地，进入递归
            self.dfs(grid, next_i, next_j, visited)

        return

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Time O(n * m)
        Space O(n * m)
        DFS写法，遇到岛屿就开始遍历四个方向，如果旁边是边界或者是海洋，说明有边界，此时周长 +1。
        另外此题可以直接两层loop整个grid，然后执行相同的逻辑，不一定需要DFS。时间上是一样的，空间上更省，不需要visited数组记录是否访问过。
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 遇到岛屿并且没有访问过开始遍历
                if grid[i][j] == 1 and visited[i][j] is False:
                    self.dfs(grid, i, j, visited)

        return self.perimeter


class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Time O(mn)
        Space O(1)
        直接两个loop遍历所有岛屿，如果上面和左边是岛屿，则 -2，因为两个边overlap。只需要check两个方向因为，每个岛屿是从上方和左边的方向
        双loop遍历的，并不需要check四个方向，这样会造成重复删除。
        """
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    # 上面是岛屿
                    if r > 0 and grid[r - 1][c] == 1:
                        result -= 2
                    # 左边是岛屿
                    if c > 0 and grid[r][c - 1] == 1:
                        result -= 2

        return result


s = Solution()
print(s.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
