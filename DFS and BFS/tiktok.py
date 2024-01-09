# Question 1
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of
# islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.

# Question 2
# If we can only flip once water to island, what is min island we can get after flipped.

# Example 1:

# Input: grid = [
#   ["0","1","0","0","0"],
#   ["1","0","1","0","0"],
#   ["0","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Question 1:
# Output: 4
# Question 2:
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Question 1:
# Output: 3
# Question 2:
# Output: 2

class Island:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(self, grid, x, y, m, n, visited, mark):

        visited[x][y] = mark
        for direction in self.directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if visited[next_x][next_y]:
                continue
            if grid[next_x][next_y] == "0":
                continue
            self.dfs(grid, next_x, next_y, m, n, visited, mark)

        return

    def get_number_island(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        mark = 2
        res = float('inf')

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and visited[x][y] is False:
                    count += 1
                    self.dfs(grid, x, y, m, n, visited, mark)
                    mark += 1

        for x in range(m):
            for y in range(n):
                if grid[x][y] == "0":
                    num_distinct_islands = set()
                    for direction in self.directions:
                        next_x = x + direction[0]
                        next_y = y + direction[1]
                        if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                            continue
                        if visited[next_x][next_y] >= 2:
                            num_distinct_islands.add(visited[next_x][next_y])
                    res = min(res, count - len(num_distinct_islands) + 1)

        return res


island_test = Island()
print(island_test.get_number_island(grid=[
    ["0", "1", "0", "0", "0"],
    ["1", "0", "1", "1", "0"],
    ["0", "1", "1", "0", "1"],
    ["0", "0", "0", "1", "0"]
]))
