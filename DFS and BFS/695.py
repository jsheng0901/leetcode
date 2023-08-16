class Solution1:
    def __init__(self):
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.count = 0

    def dfs(self, grid, visited, i, j):
        """
        DFS的一种写法，不需要判断递归停止条件，dfs只处理下一个节点，即在主函数遇到岛屿就计数为1，dfs处理接下来的相邻陆地
        """
        m = len(grid)
        n = len(grid[0])

        for d in self.dirs:
            next_x = i + d[0]
            next_y = j + d[1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if grid[next_x][next_y] == 1 and visited[next_x][next_y] is False:
                self.count += 1     # 下一个节点已经判断是岛屿，此时计数并且记录访问过
                visited[next_x][next_y] = True
                self.dfs(grid, visited, next_x, next_y)

    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        """
        Time O(m * n) 同200
        Space O(m * n)
        DFS写法，定义count和dirs为全局变量，特别是count要定义为全局
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        area = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] is False and grid[i][j] == 1:
                    visited[i][j] = True    # 标记为True
                    self.count = 1      # 因为dfs处理下一个节点，所以这里遇到陆地了就先计数，dfs处理接下来的相邻陆地
                    self.dfs(grid, visited, i, j)   # 将与其链接的陆地都标记上True
                    area = max(area, self.count)    # 每次出DFS则代表找完一个岛屿，此时更新最大面积

        return area


class Solution2:
    def __init__(self):
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.count = 0

    def dfs(self, grid, visited, i, j):
        """
        DFS的另一种写法，需要判断递归停止条件，dfs处理当前节点，即在主函数遇到岛屿就计数为0，dfs处理接下来的全部陆地
        但是处理下一个节点的方式更高效，这样可以避免没必要地递归
        """
        if grid[i][j] == 0 or visited[i][j] is True:    # 终止条件：访问过的节点或者遇到海水
            return

        m = len(grid)
        n = len(grid[0])
        visited[i][j] = True        # 标记访问过
        self.count += 1             # 开始计数

        for d in self.dirs:
            next_x = i + d[0]
            next_y = j + d[1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            self.dfs(grid, visited, next_x, next_y)

    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        """
        Time O(m * n) 同200
        Space O(m * n)
        DFS写法，定义count和dirs为全局变量，特别是count要定义为全局
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        area = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] is False and grid[i][j] == 1:
                    self.count = 0                  # 因为dfs处理当前节点，所以遇到陆地计数为0，进dfs之后在开始从1计数
                    self.dfs(grid, visited, i, j)   # 将与其链接的陆地都标记上True
                    area = max(area, self.count)    # 每次出DFS则代表找完一个岛屿，此时更新最大面积

        return area


s = Solution2()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(s.maxAreaOfIsland(grid=grid))
