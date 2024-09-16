from typing import List


class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        # 初始化列队
        queue = [start]
        visited = [[False] * n for _ in range(m)]
        visited[start[0]][start[1]] = True

        while queue:
            # 当前节点
            cur = queue.pop(0)
            # 判断是否是终点
            if [cur[0], cur[1]] == destination:
                return True

            for direction in self.directions:
                # 注意这里每次x，y的时候都要从当前节点来拿，因为x，y与之被更新在后面的loop里面
                x, y = cur[0], cur[1]
                # 如果在matrix内，并且不是墙，就一直往当前方向走
                while m > x >= 0 == maze[x][y] and 0 <= y < n:
                    x += direction[0]
                    y += direction[1]

                # 跳出循环的时候是越界或者墙，需要退回上一步
                x -= direction[0]
                y -= direction[1]

                # 如果没有访问过则可以走到
                if visited[x][y] is False:
                    queue.append([x, y])
                    visited[x][y] = True

        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """
        Time O(m * n)
        Space O(m * n)
        标准的BFS模版题，唯一的区别是每次不是走一步，而是一直往一个方向走直到遇到墙。详细见注释。
        """
        return self.bfs(maze, start, destination)


s = Solution()
print(
    s.hasPath(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
              destination=[3, 2]))
print(
    s.hasPath(maze=[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], start=[4, 3],
              destination=[0, 1]))
