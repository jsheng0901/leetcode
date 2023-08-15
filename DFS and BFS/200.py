class Solution1:
    def dfs(self, grid, i, j):
        # 当超出棋盘范围，或者是0的时候则停止
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)

        return

    def numIslands1(self, grid: [[str]]) -> int:
        """
        此题目的是找到连续为1的路径有几种，所以一直递归到四周都不是1的时候，停止递归，此时count += 1
        递归思路，每次判断当前是不是1，如果不是则跳过，
        是1则判断旁边四个是不是1，每次路过1的时候，改成0，防止loop重复的节点
        """
        if len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def numIslands2(self, grid: [[str]]) -> int:
        """
        Time O(m * n) 需要遍历所有格子
        Space O(m * n) 需要visited数组记录所有走过的格子情况
        一样的思路，但是不用写递归停止条件，而是放在进入递归的时候判断
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 四个方向
        count = 0

        def dfs(x, y):
            for d in dirs:
                next_x = x + d[0]
                next_y = y + d[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:  # 越界了，直接跳过
                    continue
                if visited[next_x][next_y] is False and grid[next_x][next_y] == '1':  # 没有访问过的同时是陆地的
                    visited[next_x][next_y] = True  # 没有访问过，立即打上True标签
                    dfs(next_x, next_y)  # 不需要递归之后回溯，因为不需要往回走

        for i in range(m):
            for j in range(n):
                if visited[i][j] is False and grid[i][j] == '1':
                    visited[i][j] = True  # 没有访问过，立即打上True标签
                    count += 1  # 遇到没访问过的陆地，+1
                    dfs(i, j)  # 将与其链接的陆地都标记上 true

        return count


class Solution2:
    def __init__(self):
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs(self, grid, visited, i, j):
        m = len(grid)
        n = len(grid[0])
        queue = [(i, j)]  # 用列队表示，这样处理的永远是列对头的元素，也就是先处理四个方向
        visited[i][j] = True  # 注意BFS的写法是一旦进入列队就要记录访问过
        while queue:
            top_x, top_y = queue.pop(0)
            for d in self.dirs:
                next_x = top_x + d[0]
                next_y = top_y + d[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                if grid[next_x][next_y] == '1' and visited[next_x][next_y] is False:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True  # 同理，记录访问过

    def numIslands(self, grid: [[str]]) -> int:
        """
        Time O(m * n) 同DFS
        Space O(m * n) 同DFS
        BFS写法，每次处理一个点的四个方向的点。
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] is False and grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, visited, i, j)

        return count


class Solution3:
    def __init__(self):
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(self, grid, visited, i, j):
        m = len(grid)
        n = len(grid[0])

        for d in self.dirs:
            next_x = i + d[0]
            next_y = j + d[1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if grid[next_x][next_y] == '1' and visited[next_x][next_y] is False:
                visited[next_x][next_y] = True
                self.dfs(grid, visited, next_x, next_y)

    def numIslands(self, grid: [[str]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        DFS全局写法，区别在于需要给DFS传入visited和grid参数
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] is False and grid[i][j] == '1':
                    visited[i][j] = True
                    count += 1
                    self.dfs(grid, visited, i, j)

        return count


s = Solution3()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
