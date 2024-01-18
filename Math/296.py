from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def bfs(self, grid, m, n, x, y):
        # BFS模版计算到所有1的距离
        queue = [(x, y)]
        visited = [[False] * n for _ in range(m)]
        visited[x][y] = True
        steps = 0
        distance = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                if grid[x][y] == 1:
                    distance += steps
                for direction in self.directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if visited[next_x][next_y]:
                        continue
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
            steps += 1

        return distance

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(m^2 * n^2)
        Space O(m * n)
        BFS遍历所有点，计算出到所有1的距离和，然后对比出最短距离和。此方法超时。
        和317这里不一样的地方是，这里需要注意的是我们遇到1的时候并不需要停下来，而且所有点都可以是起始点。
        """
        m, n = len(grid), len(grid[0])
        min_distance = float('inf')

        for x in range(m):
            for y in range(n):
                # 计算到每个1的距离和
                distance = self.bfs(grid, m, n, x, y)
                # 取最小值
                min_distance = min(min_distance, distance)

        return min_distance


class Solution2:

    def get_distance(self, points, origin):
        distance = 0

        for point in points:
            distance += abs(point - origin)

        return distance

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n + nlog(n))
        Space O(m * n)
        这题本质上是数学题，到达两点之间距离和最短的点一定是两个点或者说整个array的中位数。
        所以我们只需要找到两个维度中位数，及这个点就是到达所有点1的最短距离和点。
        统计处所有1的点，同时sorted每个维度，这里row不用sort因为loop本身就是从0开始有序的。
        找到每个维度的中位数，之后计算这个中位数点到所有1的距离和即可。
        """
        m, n = len(grid), len(grid[0])
        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        row_median = rows[len(rows) // 2]
        cols.sort()
        col_median = cols[len(cols) // 2]

        row_distance = self.get_distance(rows, row_median)
        col_distance = self.get_distance(cols, col_median)

        return row_distance + col_distance


class Solution3:
    def get_rows(self, grid, m, n):
        rows = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)

        return rows

    def get_cols(self, grid, m, n):
        cols = []
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        return cols

    def get_distance(self, points, origin):
        distance = 0

        for point in points:
            distance += abs(point - origin)

        return distance

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        整个思路和思路2是一模一样的，只是在找中位数上面我们可以通过loop的形式避免sort。row loop 从上到下，col loop 从左到右，保证有序。
        """
        m, n = len(grid), len(grid[0])
        rows = self.get_rows(grid, m, n)
        cols = self.get_cols(grid, m, n)

        row_median = rows[len(rows) // 2]
        col_median = cols[len(cols) // 2]

        row_distance = self.get_distance(rows, row_median)
        col_distance = self.get_distance(cols, col_median)

        return row_distance + col_distance


s = Solution3()
print(s.minTotalDistance(grid=[[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
