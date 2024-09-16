import heapq
from typing import List


class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dijkstra(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        # 记录走到节点的时候最短路径，同时可以防止走回头路
        visited = [[float('inf')] * n for _ in range(m)]
        # 初始化起点
        visited[start[0]][start[1]] = 0

        pq = []
        # 初始化优先列队
        heapq.heappush(pq, (0, start[0], start[1]))

        while pq:
            # 当前节点状态
            cur = heapq.heappop(pq)

            # 判断是否是终点
            if [cur[1], cur[2]] == destination:
                return visited[cur[1]][cur[2]]

            for direction in self.directions:
                # 注意这里每次x，y的时候都要从当前节点来拿，因为x，y与之被更新在后面的loop里面，同490题目
                cur_x = cur[1]
                cur_y = cur[2]
                dist = cur[0]
                # 如果在matrix内，并且不是墙，就一直往当前方向走
                while 0 <= cur_x < m and 0 <= cur_y < n and maze[cur_x][cur_y] == 0:
                    cur_x += direction[0]
                    cur_y += direction[1]
                    dist += 1

                # 跳出循环的时候是越界或者墙，需要退回上一步
                cur_x -= direction[0]
                cur_y -= direction[1]
                dist -= 1

                # 如果遇到更小的路径达到当前节点
                if dist < visited[cur_x][cur_y]:
                    # 更新距离
                    visited[cur_x][cur_y] = dist
                    # 同时节点加入优先列队
                    heapq.heappush(pq, (dist, cur_x, cur_y))

        return -1

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        Time O(m * n * log(m * n))
        Space O(m * n)
        标准的最短路径题目，用dijkstra模版写。注意这里把节点状态放进优先列队的时候，要把distance放在第一位才能达到小顶堆的效果，否则
        优先列队排序的时候对比数据不会用distance。其它要点和490一样，详细见注释。
        """
        short_dist = self.dijkstra(maze, start, destination)

        return short_dist


s = Solution()
print(s.shortestDistance(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                         start=[0, 4], destination=[4, 4]))
print(s.shortestDistance(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                         start=[0, 4], destination=[3, 2]))
