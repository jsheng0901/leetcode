import heapq
from typing import List


class Solution:
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
        Time O(n * m)
        Space O(n * m)
        本质上是 Dijkstra 模板题。区别于记录最短路径的权重和，这里到达[i][j]的意义是路径中最小权重绝对值差。
        graph里面的权重在这里是每个格子的高度。每个格子和相邻的四个方向就是graph里面相连接的边。
        """

        # 调用 Dijkstra 模板
        return self.dijkstra(heights)


s = Solution()
print(s.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
