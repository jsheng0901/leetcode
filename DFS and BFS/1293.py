from typing import List


class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(self, grid, k):
        m, n = len(grid), len(grid[0])
        # 如果我们有足够的消除步数，最短距离就是直接曼哈顿距离
        if k >= m + n - 2:
            return m + n - 2
        queue = []
        # 记录每一个节点的状态，(i, j, 剩余的k steps)
        state = (0, 0, k)
        # 记录走到每个节点的steps和状态
        queue.append((0, state))
        # 初始化起点
        visited = {state}

        while queue:
            size = len(queue)
            for _ in range(size):
                # 当前节点
                front = queue.pop(0)
                step, (i, j, k) = front[0], front[1]
                # 如果走到目的地，直接返回step
                if i == m - 1 and j == n - 1:
                    return step
                # 遍历周边四个方向
                for direction in self.directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    # 越界，跳过
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    # 下一个节点是障碍物，并且没有足够的k，跳过
                    if grid[next_i][next_j] == 1 and k == 0:
                        continue
                    # 新的 k
                    new_k = k - grid[next_i][next_j]
                    # 下一个节点的状态
                    new_state = (next_i, next_j, new_k)
                    # 如果下一个节点访问过，并且走到此节点的k也是一样的情况下，跳过，这里一定要记录k，
                    # 因为不同的path可以走到同一个节点，但是走到同一个节点的k使用情况应该不一样
                    if (next_i, next_j, new_k) in visited:
                        continue
                    # 加入新的节点进列队
                    queue.append((step + 1, new_state))
                    # 加入进访问过记录
                    visited.add(new_state)

        return -1

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Time O(n * m * k)
        Space O(n * m * k)
        worse case我们走过所有点的所有k的情况，其实是一个三维数组，同理其实visited可以用三维数组来记录所有访问情况。
        BFS模板题，此题最重要的是记录每个节点走到的状态，同一个节点可以有不同的k走到，所以必须记录并且判断查重，查重要查所有状态是否一样。
        """

        res = self.bfs(grid, k)

        return res


s = Solution()
print(s.shortestPath(grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1))
print(s.shortestPath(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1))
print(s.shortestPath(grid=[[0, 0, 0]], k=1))
print(s.shortestPath(
    grid=[[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 0],
          [0, 0]], k=4))
print(s.shortestPath(
    grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], k=1))
