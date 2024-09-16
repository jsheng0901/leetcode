import heapq
from typing import List


class Solution:
    def __init__(self):
        self.directions = [(0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'), (-1, 0, 'u')]

    def dijkstra(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        # 记录走到节点的时候最短路径，同时可以防止走回头路
        visited = [[float('inf')] * n for _ in range(m)]
        # 初始化起点
        visited[start[0]][start[1]] = 0

        pq = []
        # 初始化优先列队
        heapq.heappush(pq, (0, start[0], start[1], ''))
        # 记录所有可能的最短路径
        short_path = []

        while pq:
            # 当前节点状态
            cur = heapq.heappop(pq)

            for direction in self.directions:
                # 注意这里每次x，y的时候都要从当前节点来拿，因为x，y与之被更新在后面的loop里面，同490题目
                cur_x = cur[1]
                cur_y = cur[2]
                dist = cur[0]
                cur_d = cur[3]
                # 如果在matrix内，并且不是墙，就一直往当前方向走，同时保证不能走过终点
                while 0 <= cur_x < m and 0 <= cur_y < n and maze[cur_x][cur_y] == 0 and [cur_x, cur_y] != destination:
                    cur_x += direction[0]
                    cur_y += direction[1]
                    dist += 1

                # 跳出循环的时候是越界或者墙，或者是终点，需要退回上一步，这里如果是终点则不需要退回
                if [cur_x, cur_y] != destination:
                    cur_x -= direction[0]
                    cur_y -= direction[1]
                    dist -= 1
                else:
                    # 遇到终点，如果是第一次遇到，一定是最短路
                    if visited[cur_x][cur_y] == float('inf'):
                        # 记录路径本身
                        short_path.append(cur_d + direction[2])
                        # 更新距离
                        visited[cur_x][cur_y] = dist
                    # 如果之前遇到过，说明有同样的距离不一样的走法的路径
                    elif dist == visited[cur_x][cur_y]:
                        short_path.append(cur_d + direction[2])

                    # 跳过后续，直接进入下一个节点
                    continue

                # 因为后面允许同一个节点小于等于都可以重复访问，这里需要注意就是原地踏步的情况，所以如果是原地踏步，需要跳过
                if [cur_x, cur_y] == [cur[1], cur[2]]:
                    continue

                # 如果遇到小于等于的路径达到当前节点
                if dist <= visited[cur_x][cur_y]:
                    # 更新距离
                    visited[cur_x][cur_y] = dist
                    # 同时节点加入优先列队
                    heapq.heappush(pq, (dist, cur_x, cur_y, cur_d + direction[2]))

        return short_path

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        """
        Time O(m * n * log(m * n))
        Space O(m * n)
        505的延伸题，在最短路径的计算下，同时记录一下每个走的方向，需要注意的是这里因为可能会有多条路径一样的最短距离，所有需要保证同一个节点
        可以重复走到并且只要距离小于等于即可走到。详细见注释。
        """
        # 记录最短路径
        short_path = self.dijkstra(maze, ball, hole)

        # 如果不存在，说明是走不到
        if len(short_path) == 0:
            res = "impossible"
        else:
            # sort一下路径从大到小
            short_path.sort()
            # 返回排序后最小的那个
            res = short_path[0]

        return res


class Solution2:
    def __init__(self):
        self.directions = [(0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'), (-1, 0, 'u')]

    def dijkstra(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        # 这里我们不用visited数组记录走到节点的最短路径，因为每个节点都可以重复访问，但是为了避免回头，需要一个集合查重
        seen = set()

        pq = []
        # 初始化优先列队，并且保证一个是距离，第二个是方向，后面两个是节点本身，才能来利用优先列队自动排序
        heapq.heappush(pq, (0, '', start[0], start[1]))

        while pq:
            # 当前节点状态
            cur = heapq.heappop(pq)

            # 如果是重点，直接返回当前长度，因为第一个遇到的终点一定是最短并且字母排序最小的那个
            if [cur[2], cur[3]] == destination:
                return cur[1]

            # 如果访问过，直接跳过，这里用来查重
            if (cur[2], cur[3]) in seen:
                continue

            # 加入访问过的字典
            seen.add((cur[2], cur[3]))

            for direction in self.directions:
                # 注意这里每次x，y的时候都要从当前节点来拿，因为x，y与之被更新在后面的loop里面，同505题
                cur_x = cur[2]
                cur_y = cur[3]
                dist = cur[0]
                cur_d = cur[1]
                # 如果在matrix内，并且不是墙，就一直往当前方向走，同时保证不能走过终点
                while 0 <= cur_x < m and 0 <= cur_y < n and maze[cur_x][cur_y] == 0 and [cur_x, cur_y] != destination:
                    cur_x += direction[0]
                    cur_y += direction[1]
                    dist += 1

                # 如果不是重点，需要退回上一步
                if [cur_x, cur_y] != destination:
                    # 跳出循环的时候是越界或者墙，需要退回上一步
                    cur_x -= direction[0]
                    cur_y -= direction[1]
                    dist -= 1

                # 这里也不再需要判断，因为所有点我们都让加入列队，进行小顶堆排序
                # if [cur_x, cur_y] == [cur[1], cur[2]]:
                #     continue

                # 这里也不再需要判断，因为所有点我们都让加入列队，进行小顶堆排序
                # if dist <= visited[cur_x][cur_y]:
                # visited[cur_x][cur_y] = dist
                heapq.heappush(pq, (dist, cur_d + direction[2], cur_x, cur_y))

        return "impossible"

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        """
        Time O(m * n * log(m * n))
        Space O(m * n)
        同思路1，但是我们可以让优先列队来排序字母顺序，只需要放在第二位列队里面的元素即可，这样就不需要再对结果sort了，第一个走到终点的路径
        一定是距离最短并且字母排序最小的那条路径。同时我们也不再排序距离更新，只要能走到的都可以重复走到，加一个判断在弹出节点后。详细见注释。
        """
        # 最短路径本身
        short_path = self.dijkstra(maze, ball, hole)

        return short_path


s = Solution2()
print(s.findShortestWay(maze=[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]],
                        ball=[4, 3], hole=[0, 1]))
print(s.findShortestWay(
    maze=[[0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]], ball=[2, 4], hole=[7, 6]))
