from typing import List


class Solution1:
    """
    Time O(m*n)
    Space O(m*n), only need dfs, set compare takes O(1)
    we do the dfs store all island relative position into set, then every time add frozenset into set to compare
    """

    def numDistinctIslands(self, grid: [[int]]) -> int:
        # Do a DFS to find all cells on the current island.
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or grid[row][col] == 0:
                return
            seen.add((row, col))
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    current_island = set()
                    row_origin = row
                    col_origin = col
                    dfs(row, col)
                    if current_island:
                        unique_islands.add(frozenset(current_island))
        return len(unique_islands)


class Solution2:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def dfs(self, grid, x, y, island_string, dire):
        m, n = len(grid), len(grid[0])
        # 前序遍历位置：进入 (x, y)，当前节点处理，记录来访的方向和当前节点淹没岛屿
        grid[x][y] = 0
        island_string.append(str(dire))
        island_string.append(',')
        # 遍历四个方向
        for direction in self.directions:
            next_x = direction[0] + x
            next_y = direction[1] + y
            # 越界，跳过
            if next_x >= m or next_x < 0 or next_y >= n or next_y < 0:
                continue
            # 不是岛屿，跳过
            if grid[next_x][next_y] == 0:
                continue
            # 不同方向赋予不同的值代表
            if direction[0] == -1 and direction[1] == 0:
                dire = 1
            elif direction[0] == 1 and direction[1] == 0:
                dire = 2
            elif direction[0] == 0 and direction[1] == -1:
                dire = 3
            elif direction[0] == 0 and direction[1] == 1:
                dire = 4
            # 递归继续遍历邻居节点
            self.dfs(grid, next_x, next_y, island_string, dire)

        # 后序遍历位置：离开 (x, y)，同前序遍历的位置，只是方向变了一下
        island_string.append(str(-dire))
        island_string.append(',')

        return

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        Time O(m * n)
        Space O(m * n)
        同思路1，不同在于如何记录岛屿的样子，这里我们定义四个方向来记录岛屿DFS遍历的顺序即可代表不同的岛屿。
        假设它们的遍历顺序是：下，右，上，撤销上，撤销右，撤销下，如果我用分别用 1, 2, 3, 4 代表上下左右，
        用 -1, -2, -3, -4 代表上下左右的撤销，那么可以这样表示它们的遍历顺序：2, 4, 1, -1, -4, -2
        这就相当于是岛屿序列化的结果，只要每次使用 dfs 遍历岛屿的时候生成这串数字进行比较，就可以计算到底有多少个不同的岛屿了。
        这里还有一个小trick就是我们并不需要单独记录访问过的节点，直接在原始grid上面改岛屿变成海洋也就1 -> 0 即可。
        """
        # 记录所有岛屿的序列化结果
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果岛屿是1
                if grid[i][j] == 1:
                    # 淹掉这个岛屿，同时存储岛屿的序列化结果
                    island_string = []
                    # 初始的方向可以随便写，不影响正确性
                    self.dfs(grid, i, j, island_string, 100)
                    islands.add("".join(island_string))
        # 返回不同的岛屿数量
        return len(islands)


s = Solution2()
print(s.numDistinctIslands(grid=[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
