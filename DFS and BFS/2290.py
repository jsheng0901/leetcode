from collections import deque
from typing import List
import heapq


class Solution1:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.min_obstacles = float('inf')

    def dfs(self, grid, i, j, visited, num_obstacles):
        # 标准DFS遍历grid的框架
        m, n = len(grid), len(grid[0])
        if i == m - 1 and j == n - 1:
            self.min_obstacles = min(self.min_obstacles, num_obstacles)
            return

        visited[i][j] = True
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                continue
            if visited[next_i][next_j]:
                continue
            if grid[next_i][next_j] == 1:
                self.dfs(grid, next_i, next_j, visited, num_obstacles + 1)
            else:
                self.dfs(grid, next_i, next_j, visited, num_obstacles)

        # 注意这里要回溯，因为其它path也可以走到相同的节点
        visited[i][j] = False

        return

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        Time O(C(m, m + n)) --> O((M+N)(log(M+N)loglog(M+N))^2)
        Space O(m * n)
        直接最粗暴的方法找出所有路径，并记录每个路径要移除的障碍物的个数，走到右下角的时候最后更新最少的移除数量即可。
        时间复杂度就是计算有多少条unique path从左上角走到右下角，也就是62题的时间复杂度，比较复杂的数学推理这里。不过此题这个方法明显TLE。
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        self.dfs(grid, 0, 0, visited, 0)

        return self.min_obstacles


class Solution2:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(self, grid):
        m, n = len(grid), len(grid[0])
        # 记录是否走回头路
        visited = [[False] * n for _ in range(m)]
        # 优先列队，小顶堆，存储当前障碍物最少的点
        queue = []
        # 起始点入列队
        heapq.heappush(queue, (0, 0, 0))
        # 标记访问过
        visited[0][0] = True

        while queue:
            size = len(queue)
            for _ in range(size):
                # 遇到当前点是终点，直接返回结果，一定是遇到最少障碍物的路径，并且一定可以走到这里
                cur_obstacles, cur_i, cur_j = heapq.heappop(queue)
                if cur_i == m - 1 and cur_j == n - 1:
                    return cur_obstacles
                # 遍历四个方向
                for direction in self.directions:
                    next_i = cur_i + direction[0]
                    next_j = cur_j + direction[1]
                    # 越界，跳过
                    if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                        continue
                    # 访问过，跳过
                    if visited[next_i][next_j]:
                        continue
                    # 当前是障碍物，入列队并且障碍物个数 +1
                    if grid[next_i][next_j] == 1:
                        heapq.heappush(queue, (cur_obstacles + 1, next_i, next_j))
                    # 当前不是障碍物，入列队
                    else:
                        heapq.heappush(queue, (cur_obstacles, next_i, next_j))
                    # 标记访问过，这里不需要像DFS一样回溯，因为我们找的是最短的path走到终点，所以不会出现其它path走到同一个点的情况。
                    visited[next_i][next_j] = True

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n * log(m * n))
        Space O(m * n)
        时间复杂度，总共的点的个数乘以每次加入pq需要的操作时间。明显此题可以用BFS来解决，每次我们存储当前点遇到障碍物的个数，每次用pq来记录
        下一步所有可以走到的点中哪一个点含有的障碍物最少，就选择这个点最为下一步。每一步都选择最少地走，最终一定可以走到终点。详细见注释。
        """
        min_obstacles = self.bfs(grid)

        return min_obstacles


class Solution3:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(self, grid):
        m, n = len(grid), len(grid[0])
        # 表示 the currently minimum obstacles need to remove to reach (i, j)
        # 并且dist可以用来避免走回头路，因为走过的一定不是初始值，所以我们要走初始值的下一个点
        dist = [[float("inf")] * n for _ in range(m)]
        # 初始值是0
        dist[0][0] = 0
        # 使用双向列队，保证双向弹出和添加都是O(1)的操作时间，加入第一个访问的点
        dq = deque([(0, 0, 0)])

        while dq:
            size = len(dq)
            for _ in range(size):
                # 当前列队头节点
                cur_obstacles, cur_i, cur_j = dq.popleft()
                # 走到底了，直接返回结果
                if cur_i == m - 1 and cur_j == n - 1:
                    return cur_obstacles

                for direction in self.directions:
                    next_i = cur_i + direction[0]
                    next_j = cur_j + direction[1]
                    # 越界，跳过
                    if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                        continue
                    # 走回头路了，跳过
                    if dist[next_i][next_j] != float("inf"):
                        continue
                    # 核心思想
                    # Whenever encountering an empty cell neighbor, the dist value is same and hence we can put it to
                    # the front of the Deque; Otherwise, put it to the back of the Deque
                    # 如果当前是障碍物
                    if grid[next_i][next_j] == 1:
                        # 下一个的权重一定等于当前权重 + 1
                        dist[next_i][next_j] = cur_obstacles + 1
                        # 先处理权重小的节点，所以放在列对尾
                        dq.append((cur_obstacles + 1, next_i, next_j))
                    # 如果是空节点
                    else:
                        # 下一个的权重一定等于当前权重
                        dist[next_i][next_j] = cur_obstacles
                        # 先处理权重小的节点，所以放在列对头
                        dq.appendleft((cur_obstacles, next_i, next_j))

        return dist[-1][-1]

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        0-1 BFS的标准写法，对于0-1 BFS就是当权重只有0或者1的时候找最短path的方式，
        核心逻辑就是走到当前位置的时候权重 + 下一个边的权重 < 下一个点的权重的时候，我们来判断下一个点的是0还是1，如果是1，说明排在列队最后，
        如果是0，说明加入列队头，先处理。这里因为不需要每次都用优先列队排序权重，所以省去了对于每次优先列队的操作log(m * n)的时间。
        本质上就是保证和无权图BFS遍历一样，每次弹出的节点权重一定是最小的，在列队里面的节点是按照权重大小从小到大排列的顺序，所以可以每次都
        弹出列对头，保证弹出的那个权重一定是最小的。
        """
        min_obstacles = self.bfs(grid)

        return min_obstacles


class Solution4:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dijkstra(self, grid):
        m, n = len(grid), len(grid[0])
        # 同0-1BFS写法，用dist数组记录走到当前位置的权重，并且用来避免走回头路
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        pq = []
        # 初始值入列队
        heapq.heappush(pq, (0, 0, 0))

        while pq:
            cur_obstacles, cur_i, cur_j = heapq.heappop(pq)
            # 遇到终点，直接返回
            if cur_i == m - 1 and cur_j == n - 1:
                return cur_obstacles

            for direction in self.directions:
                next_i = cur_i + direction[0]
                next_j = cur_j + direction[1]

                if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                    continue
                # if dist[next_i][next_j] != inf:
                #     continue
                # 如果当前权重加上下一个权重小于下一步的权重，那么我们就可以走这一步，并且更新下一步的权重值
                next_dist = cur_obstacles + grid[next_i][next_j]
                if next_dist < dist[next_i][next_j]:
                    # 更新下一步点的权重
                    dist[next_i][next_j] = next_dist
                    # 入优先列队下一个点
                    heapq.heappush(pq, (next_dist, next_i, next_j))

        return dist[-1][-1]

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n * log(m * n))
        Space O(m * n)
        标准的Dijkstra写法，找最短权重和的path。详细见注释。其实这个思路和思路二很像，只是这里用dist数组避免了重复visited数组。
        """
        min_obstacles = self.dijkstra(grid)

        return min_obstacles


s = Solution3()
print(s.minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
print(s.minimumObstacles(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))
print(s.minimumObstacles(grid=
                         [[0, 0, 1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                          [1, 1, 0, 1, 1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                          [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]]))
