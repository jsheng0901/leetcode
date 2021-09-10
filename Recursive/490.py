class Solution:
    def hasPath(self, maze: [[int]], start: [int], destination: [int]) -> bool:
        """
        O(n*m) time, O(n*m) space, loop all points and store all inside visited
        dfs search when go one direction keep go until it hit wall or out, then do dfs, dfs only turn the direction
        """
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(maze)
        col = len(maze[0])
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return False

            visited.add((i, j))

            if i == destination[0] and j == destination[1]:
                return True

            for dx, dy in direction:
                r, c = i, j

                while 0 <= r < row and 0 <= c < col and maze[r][c] == 0:
                    r += dx
                    c += dy

                if r != destination[0] or c != destination[1]:
                    r -= dx
                    c -= dy

                if dfs(r, c):
                    return True

            return False

        return dfs(start[0], start[1])