class Solution1:
    def __init__(self):
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.count = 0

    def dfs(self, grid, i, j):
        """
        不用写递归判断，因为进入递归的数据都是在loop里面判断过的
        """
        m = len(grid)
        n = len(grid[0])

        # 改变岛屿变成海洋
        grid[i][j] = 0
        self.count += 1

        for d in self.dirs:
            next_i = i + d[0]
            next_j = j + d[1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            if grid[next_i][next_j] == 0:
                continue
            # 进入dfs的数据都是合理的下一个坐标
            self.dfs(grid, next_i, next_j)

    def numEnclaves(self, grid: [[int]]) -> int:
        """
        Time O(m * n) 多次loop完整个grid
        Space O(1) 没有额外空间，直接在grid上面改
        DFS写法，本题要求找到不靠边的陆地面积，那么我们只要从周边找到陆地然后通过dfs或者bfs将周边靠陆地且相邻的陆地都变成海洋，
        然后再去重新遍历地图的时候，统计此时还剩下的陆地就可以了。
        """
        m = len(grid)
        n = len(grid[0])

        # 从左侧边，和右侧边 向中间遍历
        for i in range(m):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0)
            if grid[i][n - 1] == 1:
                self.dfs(grid, i, n - 1)

        # 从上边和下边 向中间遍历
        for j in range(n):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j)
            if grid[m - 1][j] == 1:
                self.dfs(grid, m - 1, j)

        # 计数重置，因为前面的计数不算
        # 重新开始数有多少个岛屿1
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)

        return self.count


class Solution2:
    def __init__(self):
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.count = 0

    def bfs(self, grid, i, j):

        m = len(grid)
        n = len(grid[0])
        # 初始化列队，加入第一个发现为1的岛屿
        queue = [(i, j)]
        # 改变岛屿变成海洋并计数
        grid[i][j] = 0
        self.count += 1

        while queue:
            top_i, top_j = queue.pop(0)
            for d in self.dirs:
                next_i = top_i + d[0]
                next_j = top_j + d[1]
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                    continue
                if grid[next_i][next_j] == 0:
                    continue
                # 加入符合的邻居岛屿，并改变成海洋并计数
                queue.append((next_i, next_j))
                self.count += 1
                grid[next_i][next_j] = 0

    def numEnclaves(self, grid: [[int]]) -> int:
        """
        Time O(m * n) 多次loop完整个grid
        Space O(1) 没有额外空间，直接在grid上面改
        BFS写法
        """
        m = len(grid)
        n = len(grid[0])

        # 从左侧边，和右侧边 向中间遍历
        for i in range(m):
            if grid[i][0] == 1:
                self.bfs(grid, i, 0)
            if grid[i][n - 1] == 1:
                self.bfs(grid, i, n - 1)

        # 从上边和下边 向中间遍历
        for j in range(n):
            if grid[0][j] == 1:
                self.bfs(grid, 0, j)
            if grid[m - 1][j] == 1:
                self.bfs(grid, m - 1, j)

        # 计数重置，因为前面的计数不算
        # 重新开始数有多少个岛屿1
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)

        return self.count


s = Solution2()
print(s.numEnclaves(
    [[0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
     [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
     [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
     [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
     [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
     [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
     [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]]
))
