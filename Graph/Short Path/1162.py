from typing import List


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, grid):
        m, n = len(grid), len(grid[0])
        # 记录是否重新访问过
        visited = [[False] * n for _ in range(m)]
        queue = []
        # 初始化所有陆地，加入起点，这里不需要标记起点是否访问过，因为对于所有陆地之后都会跳过
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # 如果都是陆地或者都是海洋，直接返回 -1
        if not queue or len(queue) == m * n:
            return -1

        dist = 0
        # 开始BFS遍历
        while queue:
            # 记录层数
            size = len(queue)
            for _ in range(size):
                cur_x, cur_y = queue.pop(0)
                for direction in self.directions:
                    next_x = cur_x + direction[0]
                    next_y = cur_y + direction[1]
                    # 越界，跳过
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    # 陆地，跳过
                    if grid[next_x][next_y] == 1:
                        continue
                    # 访问过，跳过
                    if visited[next_x][next_y]:
                        continue
                    # 新的海洋，加入列队
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

            # 更新走过的层数就是距离
            dist += 1

        return dist - 1

    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        多源BFS题型，反向思考，如果从陆地出发，到达最远的海洋是多少，这样我们把所有陆地同时出发，BFS能走到最远的海洋就是最远的距离，这里需要
        注意的是，不能重复访问，遇到陆地跳过。统计走过的层数即可。
        """
        max_dist = self.bfs(grid)

        return max_dist


class Solution2:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, grid):
        m, n = len(grid), len(grid[0])
        # 记录到达海洋的最短距离
        visited = [[float('inf')] * n for _ in range(m)]
        queue = []
        # 初始化所有陆地加入列队，这里不需优先列队，因为我们不是找最短的某一条path
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        while queue:
            cur_x, cur_y, cur_dist = queue.pop(0)

            for direction in self.directions:
                next_x = cur_x + direction[0]
                next_y = cur_y + direction[1]
                next_dist = cur_dist + 1
                # 越界，跳过
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                # 陆地，跳过
                if grid[next_x][next_y] == 1:
                    continue
                # 如果到达下一个海洋的距离更新，则更新此距离
                if next_dist < visited[next_x][next_y]:
                    visited[next_x][next_y] = next_dist
                    queue.append((next_x, next_y, next_dist))

        return visited

    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n * 2)
        Space O(m * n)
        思路和上面1的几乎一样的，但是这里类似 dijkstra 的思路，记录到达每个海洋的最短距离，再从最短距离里面找出最长的距离即可。就是要遍历
        两次grid，有点浪费。
        """
        visited = self.bfs(grid)
        # 拿到到达所有海洋的最短距离之后，找出最大的那个
        max_distance = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    max_distance = max(max_distance, visited[i][j])

        return -1 if max_distance == float('-inf') or max_distance == float('inf') else max_distance


s = Solution()
print(s.maxDistance(grid=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
