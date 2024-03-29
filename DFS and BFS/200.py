# BFS搜索模版
# dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 表示四个方向
# grid 是地图，也就是一个二维数组
# visited标记访问过的节点，不要重复访问
# x,y 表示开始搜索节点的下标
# def bfs(grid, visited, x, y):
#     queue = [(x, y)]    # 定义队列并且起始节点加入队列
#     visited[x][y] = True    # 只要加入队列，立刻标记为访问过的节点
#     while queue:     # 开始遍历队列里的元素
#         cur = queue.pop(0)  # 从队列取头元素
#         cur_x = cur[0]
#         cur_y = cur[1]   # 当前节点坐标
#         for d in dirs:   # 开始想当前节点的四个方向左右上下去遍历
#             next_x = cur_x + d[0]
#             next_y = cur_y + d[1]   # 获取周边四个方向的坐标
#             if next_x < 0 or next_x >= grid.size() or next_y < 0 or next_y >= grid[0].size():
#                 continue    # 坐标越界了，直接跳过
#             if !visited[next_x][next_y]:  # 如果节点没被访问过
#                 queue.append((next_x, next_y))  # 队列添加该节点为下一轮要遍历的节点
#                 visited[next_x][next_y] = True      # 只要加入队列立刻标记，避免重复访问


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


class Solution4:
    def __init__(self):
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        # 用列队表示，这样处理的永远是列对头的元素，也就是先处理四个方向
        queue = [(i, j)]
        # 这里直接标记在原始grid上面，不用visited数组单独记录
        grid[i][j] = "0"
        while queue:
            top_x, top_y = queue.pop(0)
            for d in self.dirs:
                next_x = top_x + d[0]
                next_y = top_y + d[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                if grid[next_x][next_y] == '1':
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = "0"  # 同理，记录访问过

    def numIslands(self, grid: [[str]]) -> int:
        """
        Time O(m * n) 同DFS
        Space O(min(m, n)) 极端case，特别窄的grid，queue里面最多放置最短边的长度的元素，长的那边会逐步逼近而不是一次性全部放进去。
        BFS写法，每次处理一个点的四个方向的点。但是不用专门开一个visited数组记录是否访问过，在原来的grid上面直接改。并且BFS可以更省空间。
        """
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)

        return count


s = Solution4()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
