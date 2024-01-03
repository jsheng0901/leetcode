from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

    def bfs(self, grid):
        # 获取矩阵大小
        m, n = len(grid), len(grid[0])
        # 初始化队列，并且将起点加入队列，并标记为已访问，这里用覆盖的方法来标记走过的点为1
        # 存储三个数据 (x, y, step)
        queue = [(0, 0, 1)]
        grid[0][0] = 1

        while queue:
            # 当前节点状态
            x, y, step = queue.pop(0)
            # 走到终点，直接返回步数
            if x == m - 1 and y == n - 1:
                return step

            # 遍历8个方向
            for direction in self.directions:
                next_x = x + direction[0]
                next_y = y + direction[1]
                # 越界，跳过
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                # 不是clean path或者已经访问过，跳过
                if grid[next_x][next_y] == 1:
                    continue
                # 加入列队合理的下一个节点，记得更新step
                queue.append((next_x, next_y, step + 1))
                # 标记访问过
                grid[next_x][next_y] = 1

        # 如果无法到达终点，则返回 -1
        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Time O(n)
        Space O(n)
        BFS模版题，区别就是四个方向变成8个方向。然后这里用节点带当前步骤的方法写，把走到当前节点的步骤状态存在节点信息里面。每次queue弹出，
        拿到走到当前节点的步数。
        """
        # 如果起点或终点为障碍物，则无法到达终点
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        return self.bfs(grid)


class Solution2:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]

    def bfs(self, grid):
        m, n = len(grid), len(grid[0])
        queue = [(0, 0)]
        grid[0][0] = 1
        # 记录路径长度
        step = 1

        while queue:
            size = len(queue)
            # 遍历当前层的所有节点
            for _ in range(size):
                x, y = queue.pop(0)

                if x == m - 1 and y == n - 1:
                    return step

                for direction in self.directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if grid[next_x][next_y] == 1:
                        continue
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = 1

            # 当前层结束遍历，下一层开始，层数增加
            step += 1

        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Time O(n)
        Space O(n)
        同思路1，只是换一个记录步数的方法。
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        return self.bfs(grid)


s = Solution2()
print(s.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
