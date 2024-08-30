from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(self, i, j, m, n, heights, visited):
        # 记录当前访问过的节点
        visited.add((i, j))
        for direction in self.directions:
            # 邻居节点
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 越界，跳过
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                continue
            # 访问过，跳过
            if (next_i, next_j) in visited:
                continue
            # 邻居低于当前节点，不可能反过来流水，跳过
            if heights[next_i][next_j] < heights[i][j]:
                continue

            self.dfs(next_i, next_j, m, n, heights, visited)

        return

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time O(m * n)
        Space O(m * n)
        从两边的大海的角度思考，四个边往中间走，如果两边大海都能最终走到的重复的cell则为我们要的结果。DFS的版本写法。
        """
        m, n = len(heights), len(heights[0])

        # 先遍历太平洋的边界
        pacific_visited = set()
        for j in range(n):
            if (0, j) not in pacific_visited:
                self.dfs(0, j, m, n, heights, pacific_visited)

        for i in range(m):
            if (i, 0) not in pacific_visited:
                self.dfs(i, 0, m, n, heights, pacific_visited)

        # 遍历大西洋的边界
        atlantic_visited = set()
        for j in range(n):
            if (m - 1, j) not in atlantic_visited:
                self.dfs(m - 1, j, m, n, heights, atlantic_visited)

        for i in range(m):
            if (i, n - 1) not in atlantic_visited:
                self.dfs(i, n - 1, m, n, heights, atlantic_visited)

        # 取交集
        ans = list(pacific_visited.intersection(atlantic_visited))

        return ans


class Solution2:
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs(self, m, n, heights, queue, visited):
        # BFS版本写法，思路同DSF
        while queue:
            (i, j) = queue.pop(0)
            for direction in self.directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                    continue
                if (next_i, next_j) in visited:
                    continue
                if heights[next_i][next_j] < heights[i][j]:
                    continue
                queue.append((next_i, next_j))
                visited.add((next_i, next_j))

        return

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time O(m * n)
        Space O(m * n)
        BFS的写法，先把所有边界点加入对应的列队，之后思路和DFS一样，只是换个写法。
        """
        m, n = len(heights), len(heights[0])

        # BFS记录访问过的节点和当前走到的节点，遍历太平洋的边界
        pacific_visited = set()
        pacific_queue = []
        for j in range(n):
            pacific_queue.append((0, j))
            pacific_visited.add((0, j))
            self.bfs(m, n, heights, pacific_queue, pacific_visited)

        for i in range(m):
            pacific_queue.append((i, 0))
            pacific_visited.add((i, 0))
            self.bfs(m, n, heights, pacific_queue, pacific_visited)

        # BFS记录访问过的节点和当前走到的节点，遍历大西洋的边界
        atlantic_visited = set()
        atlantic_queue = []
        for j in range(n):
            atlantic_queue.append((m - 1, j))
            atlantic_visited.add((m - 1, j))
            self.bfs(m, n, heights, atlantic_queue, atlantic_visited)

        for i in range(m):
            atlantic_queue.append((i, n - 1))
            atlantic_visited.add((i, n - 1))
            self.bfs(m, n, heights, atlantic_queue, atlantic_visited)

        # 取交集
        ans = list(pacific_visited.intersection(atlantic_visited))

        return ans


s = Solution2()
print(s.pacificAtlantic(heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(s.pacificAtlantic(heights=[[1]]))
