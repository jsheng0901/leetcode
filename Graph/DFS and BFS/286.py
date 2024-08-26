from collections import deque
from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, rooms, i, j, m, n, visited):
        # 加入列队
        queue = [(i, j)]
        # 标记访问过
        visited[i][j] = True
        # 初始化第一步
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                # 当前节点
                cur_i, cur_j = queue.pop(0)
                # 更新走到当前节点的最短距离
                rooms[cur_i][cur_j] = min(rooms[cur_i][cur_j], step)

                for direction in self.directions:
                    next_i = cur_i + direction[0]
                    next_j = cur_j + direction[1]
                    # 越界，跳过
                    if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                        continue
                    # 访问过，跳过
                    if visited[next_i][next_j]:
                        continue
                    # 遇到墙，跳过
                    if rooms[next_i][next_j] == -1:
                        continue
                    # 遇到另一个门，跳过
                    if rooms[next_i][next_j] == 0:
                        continue
                    # 新的节点加入列队
                    queue.append((next_i, next_j))
                    # 标记访问过
                    visited[next_i][next_j] = True
            # 更新步数
            step += 1

        return

    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        """
        Time O(m * n * m * n)
        Space O(m * n)
        对于每个门，我们遍历一次BFS找到走到room的最短距离，更新每次走到的最短距离。这个方法尽然可以过所有的TC。
        """
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                # 遇到门了
                if rooms[i][j] == 0:
                    # 构建数组防止走回头
                    visited = [[False] * n for _ in range(m)]
                    self.bfs(rooms, i, j, m, n, visited)

        return rooms


class Solution2:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, rooms, queue, m, n):
        while queue:
            # 当前节点，这里用双向列队达到真正意义上的O(1)
            # 注意我们不需要在这里进行距离的更新，因为我们完全可以在下面加入列队的时候计算距离，这样rooms数组会立马被更新访问过的room节点
            # 如果在弹出后再更新，当同一层节点很多的时候，判断是否是没有访问过的room的地方会失效，也就会导致很多节点没必要的先加入进了列队
            # 会严重拖慢遍历双向列队的速度，因为加入的节点太多了。
            cur_i, cur_j = queue.popleft()
            for direction in self.directions:
                next_i = cur_i + direction[0]
                next_j = cur_j + direction[1]
                # 越界，跳过
                if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n:
                    continue
                # 访问的节点是障碍物或者已经计算出最短距离了，跳过，这里的查重对应后面立即更新最短记录很重要，
                # 否则会出现上面说的，添加了很多没必要访问的节点，另一个需要注意的是，这里要用数值来判断是不是inf，不能用float('inf')
                if rooms[next_i][next_j] != 2147483647:
                    continue
                # 直接立即更新最短距离，这里最短距离就等于上一步最短距离 + 1，起始点门对应的值刚好是0
                rooms[next_i][next_j] = rooms[cur_i][cur_j] + 1
                # 加入列队
                queue.append((next_i, next_j))

        return

    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        """
        Time O(m * n)
        Space O(1)
        BFS有一个特点，如果走到某一步，那么当前走到的这个步数一定是最短距离，所以结合着一个特点，我们并不需要一个一个遍历门，完全可以一起遍历
        所有门的节点，因为就算同一个room，那个门先走到一定是最短距离，并且不需要再次走到这个门了。同时我们可以通过不等于room的值来判断是否
        访问过，不需要visited数组。详细见注释。
        """
        m, n = len(rooms), len(rooms[0])
        # 用双向列队，真正达到O(1)的弹出
        queue = deque()
        for i in range(m):
            for j in range(n):
                # 把所有的门放入队列，作为 BFS 遍历的起点
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # 开始执行 BFS 算法，根据 BFS 算法的特性，第一次遍历到新节点所走的步数就是最短距离，无论是哪一个起点
        self.bfs(rooms, queue, m, n)
        return rooms


s = Solution2()
print(s.wallsAndGates(
    rooms=[[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
           [0, -1, 2147483647, 2147483647]]))
