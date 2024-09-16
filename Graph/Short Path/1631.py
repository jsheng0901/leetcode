import heapq
from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dijkstra(self, heights):
        m = len(heights)
        n = len(heights[0])

        # 定义：从 (0, 0) 到 (i, j) 的最小体力消耗是 effort_to[i][j]
        effort_to = [[float('inf')] * n for _ in range(m)]
        # base case，起点到起点的最小消耗就是 0
        effort_to[0][0] = 0

        # 优先级队列，effort_from_start 较小的排在前面
        pq = []
        # 从起点 (0, 0) 开始进行 BFS。这里我们也可以不用一个class表示节点状态，用list表示状态 -> [x的位置，y的位置，x -> y 的权重]
        heapq.heappush(pq, [0, 0, 0])

        while pq:
            # 当前节点状态
            curr_state = heapq.heappop(pq)
            cur_x = curr_state[0]
            cur_y = curr_state[1]
            curr_effort_from_start = curr_state[2]

            # 到达终点提前结束
            if cur_x == m - 1 and cur_y == n - 1:
                return curr_effort_from_start

            # 如果有跟短的路径，提前结束
            if curr_effort_from_start > effort_to[cur_x][cur_y]:
                continue

            # 将当前节点的相邻坐标装入队列
            for dirs in self.directions:
                # 下一个节点坐标
                next_x = cur_x + dirs[0]
                next_y = cur_y + dirs[1]
                # 检查是否越界
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue

                # 计算从当前节点达到下一个节点的消耗
                height_diff = abs(heights[cur_x][cur_y] - heights[next_x][next_y])
                # 保存最大消耗
                effort_to_next_node = max(effort_to[cur_x][cur_y], height_diff)
                # 更新备忘录
                if effort_to_next_node < effort_to[next_x][next_y]:
                    effort_to[next_x][next_y] = effort_to_next_node
                    # 进入列队的状态 list 与一开始定义的顺序一直
                    heapq.heappush(pq, [next_x, next_y, effort_to_next_node])

        # 正常情况不会走到这里，因为一定有终点
        return -1

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Time O(m * n * log(m * n))
        Space O(m * n + m * n)
        本质上是 Dijkstra 模板题。区别于记录最短路径的权重和，这里到达[i][j]的意义是路径中最小权重绝对值差。
        graph里面的权重在这里是每个格子的高度。每个格子和相邻的四个方向就是graph里面相连接的边。
        """

        # 调用 Dijkstra 模板
        return self.dijkstra(heights)


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Time O(m * n * log(m * n) + m * n * alpha(m * n)) -> O(m * n * log(m * n))
        Space O(m * n)
        并查集的思路，我们先计算出所有点到邻居节点的高度差权重，并且把2D的matrix拉平到1D的维度，这里有个trick是2D边1D的方式为
        (currentRow, currentCol) -> currentRow * col + currentCol，这样可以方便放进并查集。再按照权重进行sort，每次
        把权重最小的两个点进行连接，直到起点和终点都已经被连接起来，此时的最小权重就是我找到的最小高度差在起点到终点的path上。
        """
        row_size = len(heights)
        col_size = len(heights[0])
        size = row_size * col_size
        edges = []
        # 计算每个点到邻居点的高度差，注意这里只有两个方向，分别是下和左，因为右和上方向已经在之前的节点计算过了高度差。
        for row in range(row_size):
            for col in range(col_size):
                # 需要计算当前节点的下一行的邻居
                if row < row_size - 1:
                    # 当前节点2D变成1D的index
                    x = row * col_size + col
                    # 邻居节点2D变成1D的index
                    y = (row + 1) * col_size + col
                    # 高度差
                    h = abs(heights[row][col] - heights[row + 1][col])
                    edges.append([x, y, h])
                # 计算当前节点的左边列的邻居
                if col < col_size - 1:
                    # 同上
                    x = row * col_size + col
                    y = row * col_size + col + 1
                    h = abs(heights[row][col] - heights[row][col + 1])
                    edges.append([x, y, h])

        # sort权重
        edges.sort(key=lambda x: x[2])

        union_find = UnionFind(size)

        # 开始遍历所有边
        for edge in edges:
            x, y, h = edge[0], edge[1], edge[2]
            # 链接当前权重最小的边
            union_find.union(x, y)
            # 如果起点和终点已经被连接起来了，说明找到了权重最小的path
            if union_find.is_connected(0, size - 1):
                return h

        return 0


class Solution3:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(self, heights, mid):
        # 标准BFS遍历graph的写法
        row, col = len(heights), len(heights[0])
        visited = [[False] * col for _ in range(row)]
        queue = [(0, 0)]
        visited[0][0] = True

        while queue:
            x, y = queue.pop(0)
            if x == row - 1 and y == col - 1:
                return True

            for direction in self.directions:
                next_x = x + direction[0]
                next_y = y + direction[1]

                if next_x < 0 or next_x >= row or next_y < 0 or next_y >= col:
                    continue
                if visited[next_x][next_y]:
                    continue
                # 计算difference值
                diff = abs(heights[next_x][next_y] - heights[x][y])
                # 保证加入进path的节点都满足小于target值
                if diff <= mid:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True

        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Time O(m * n * log(10^6))
        Space O(m * n)
        因为我们知道搜索的effort的边界区间，并且我们知道如果找到一条path可以保证最大权重小于搜索的target，那么就说明可能存在另一条path
        最大权重在target的左边，同理大于则在右边。这里我们就可以用二分法的思路来进行effort值的区间搜索。每次执行BFS看能不能找到一条从
        起点到终点的path，每次的权重都小于target值。如果图很大但是搜索区间很小的时候，也就是 m * n >> 10^6的时候，
        此方法虽然看起来要遍历很多此graph但是每次只需要找到一条path，并且不需要sort，整体来说更快。
        """
        # 搜索区间
        left = 0
        right = 10000000

        # 二分法
        while left <= right:
            mid = left + (right - left) // 2
            # 如果可以找到一条合理的起点到终点的path，说明应该去左区间继续搜索
            if self.bfs(heights, mid):
                right = mid - 1
            # 如果不能找到说明需要扩大target值
            else:
                left = mid + 1

        # 去循环的时候是left = right - 1，此时left = right也就是mid是最后的最小effort值
        return left


s = Solution2()
print(s.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
