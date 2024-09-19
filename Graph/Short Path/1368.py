import heapq
from typing import List


class Solution:
    def __init__(self):
        self.directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

    def dijkstra(self, grid):
        # dijkstra模版
        m, n = len(grid), len(grid[0])
        # 记录走到节点的时候最短路径，同时可以防止走回头路
        visited = [[float('inf')] * n for _ in range(m)]
        # 初始化起点
        visited[0][0] = 0

        pq = []
        # 初始化优先列队
        heapq.heappush(pq, (0, 0, 0))

        while pq:
            # 当前节点状态
            cost, x, y = heapq.heappop(pq)

            # 判断是否是终点
            if x == m - 1 and y == n - 1:
                return cost

            # 这里一个小技巧，四个方向用字典进行map
            for direction in range(1, 5):
                # 步长
                step = self.directions[direction]
                next_x = x + step[0]
                next_y = y + step[1]

                # 越界，跳过
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue

                # 判断走到下一个合理节点的权重
                cost_to_next_node = cost if direction == grid[x][y] else cost + 1

                # 如果遇到更小的权重路径达到下一个节点
                if cost_to_next_node < visited[next_x][next_y]:
                    # 更新距离
                    visited[next_x][next_y] = cost_to_next_node
                    # 同时节点加入优先列队
                    heapq.heappush(pq, (cost_to_next_node, next_x, next_y))

        return -1

    def minCost(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n * log(m * n))
        Space O(m * n)
        标准的最短路径写法，转化一个思路，如果不改变方向则权重是0，如果改变方向权重是1，之后就是标准的dijkstra模版写。
        """
        return self.dijkstra(grid)


s = Solution()
print(s.minCost(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))
