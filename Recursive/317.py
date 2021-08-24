class Solution1:
    def is_valid(self, grid, i, j, visited):
        if i < 0 or i >= len(grid):
            return False
        elif j < 0 or j >= len(grid[0]):
            return False
        elif visited[i][j] == 1:
            return False
        elif grid[i][j] == 2:
            return False

        return True

    def shortestDistance(self, grid: [[int]]) -> int:
        num_of_house = 0
        min_distance = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_of_house += 1

        def bfs(grid, i, j, total_house):
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            distance_sum = 0
            house_reached = 0

            queue = [[i, j]]

            visited = [[0] * len(grid[0]) for _ in range(len(grid))]
            visited[i][j] = 1
            steps = 0

            while len(queue) > 0 and house_reached != total_house:
                size = len(queue)
                for i in range(size):
                    front = queue.pop(0)
                    curr_i, curr_j = front[0], front[1]

                    if grid[curr_i][curr_j] == 1:
                        distance_sum += steps
                        house_reached += 1
                        continue

                    for dire in direction:
                        new_i = curr_i + dire[0]
                        new_j = curr_j + dire[1]
                        if self.is_valid(grid, new_i, new_j, visited):
                            visited[new_i][new_j] = 1
                            queue.append([new_i, new_j])
                steps += 1

            if house_reached != total_house:
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 0 and visited[i][j] == 1:
                            grid[i][j] == 2
                return float('inf')
            else:
                return distance_sum

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    distance = bfs(grid, i, j, num_of_house)
                    # if distance != float('inf'):
                    min_distance = min(min_distance, distance)
                    # else:
                    #     print((i, j))
                    #     return -1

        return -1 if min_distance == float('inf') else min_distance


class Solution2:
    def shortestDistance(self, grid: [[int]]) -> int:
        """bfs search, 从building的角度找0"""
        total_house = 0
        min_distance = float('inf')
        distance = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]    # 用双loop不要用 *len(grid[0])

        def bfs(grid, i, j, distance):
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = [[i, j]]

            visited = [[0] * len(grid[0]) for _ in range(len(grid))]
            visited[i][j] = 1
            steps = 0

            while len(queue) > 0:
                size = len(queue)
                for i in range(size):
                    front = queue.pop(0)
                    curr_i, curr_j = front[0], front[1]

                    if grid[curr_i][curr_j] == 0:
                        distance[curr_i][curr_j][0] += steps
                        distance[curr_i][curr_j][1] += 1

                    for dire in direction:
                        new_i = curr_i + dire[0]
                        new_j = curr_j + dire[1]
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                            if visited[new_i][new_j] == 0 and grid[new_i][new_j] == 0:
                                visited[new_i][new_j] = 1
                                queue.append([new_i, new_j])
                steps += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_house += 1
                    bfs(grid, i, j, distance)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if distance[i][j][1] == total_house:
                    min_distance = min(min_distance, distance[i][j][0])

        return -1 if min_distance == float('inf') else min_distance


s = Solution2()
print(s.shortestDistance(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
# print(s.shortestDistance(
#     [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
#      [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]))
