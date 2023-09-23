from typing import List


class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.count = 0

    def dfs(self, grid, i, j, mark, visited):

        m = len(grid)
        n = len(grid[0])
        # 标记访问过此陆地
        visited[i][j] = True
        # 给陆地标记新标签
        grid[i][j] = mark
        # 记录岛屿陆地数量
        self.count += 1

        for d in self.directions:
            next_i = i + d[0]
            next_j = j + d[1]
            # 越界
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            # 访问过或者邻居是海洋
            if visited[next_i][next_j] or grid[next_i][next_j] == 0:
                continue
            self.dfs(grid, next_i, next_j, mark, visited)

        return

    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        先遍历整个graph，给所有本身是岛屿的格子打上标签，然后同时记录每个岛屿标签下的大小。然后遍历打过标签的grid，同时翻转每个海洋变成岛屿，
        如果反转后形成新的大岛屿，则根据之前打过标签的大小记录新的岛屿大小。同时更新最大值。
        """
        m = len(grid)
        n = len(grid[0])
        # 标记访问过的点
        visited = [[False] * n for _ in range(m)]
        # 记录岛屿每个编号对应的大小
        island_number = {}
        # 标记是否整张地图都是陆地
        is_all_land = True
        # 记录每个岛屿的编号
        mark = 2
        # 记录最终结果
        size = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    is_all_land = False
                if grid[i][j] == 1 and visited[i][j] is False:
                    # 初始化计算岛屿大小的变量
                    self.count = 0
                    # 将与其链接的陆地都标记上 true
                    self.dfs(grid, i, j, mark, visited)
                    # 走完一个岛屿，记录此编号对应的岛屿大小
                    island_number[mark] = self.count
                    # 岛屿的编号 +1
                    mark += 1

        # 如果都是陆地，返回全面积
        if is_all_land:
            size = m * n
            return size

        # 以下逻辑是根据添加陆地的位置，计算周边岛屿面积之和
        for i in range(m):
            for j in range(n):
                # 记录连接之后的岛屿数量
                count = 1
                # 每次使用时，清空，初始化访问过的岛屿编号
                visited_island = set()
                if grid[i][j] == 0:
                    for d in self.directions:
                        next_i = i + d[0]
                        next_j = j + d[1]
                        # 越界
                        if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                            continue
                        # 添加过的岛屿不要重复添加
                        if grid[next_i][next_j] in visited_island:
                            continue
                        # 邻居是海洋直接跳过
                        if grid[next_i][next_j] == 0:
                            continue
                        # 把相邻四面的岛屿数量加起来
                        count += island_number[grid[next_i][next_j]]
                        # 标记该岛屿已经添加过
                        visited_island.add(grid[next_i][next_j])

                size = max(size, count)

        return size


s = Solution()
print(s.largestIsland([[1, 0], [0, 1]]))
