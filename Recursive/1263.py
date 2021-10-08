from collections import deque


class Solution:
    def minPushBox(self, grid: [[str]]) -> int:
        """
        整体逻辑就是，现在找到三个点的位置，对box做BFS search，每次box动的时候判断person是否也可以到达新的位置，
        最终找到target， BFS优势是找最短路径，同时不符合的路径不会进列队，所以queue长度为0的时候也就是结束的时候
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # find B, S, T position
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 'B':
                    box = (i, j)
                if grid[i][j] == 'S':
                    person = (i, j)
                if grid[i][j] == 'T':
                    target = (i, j)

        def isvalid(x, y):
            return 0 <= x < self.m and 0 <= y < self.n and grid[x][y] != '#'

        def check(curr, dest, box):
            """check original person position if can reach to new person position, BFS search again"""
            q = deque()
            q.append(curr)
            visited = set(curr)
            while q:
                curr = q.popleft()

                if curr == dest:
                    return True

                for dir_ in self.dirs:
                    r = curr[0] + dir_[0]
                    c = curr[1] + dir_[1]

                    if isvalid(r, c) and (r, c) not in visited and (r, c) != box:
                        q.append((r, c))
                        visited.add((r, c))
            return False
        # 初始化双向列队
        q = deque([(0, box, person)])

        visited = set((box, person))

        while q:
            dis, box, person = q.popleft()

            if box == target:
                return dis

            for dir_ in self.dirs:

                new_box_x = dir_[0] + box[0]
                new_box_y = dir_[1] + box[1]

                # person is always behind box, box 和 person是相反的方向
                new_person_x = box[0] - dir_[0]
                new_person_y = box[1] - dir_[1]

                new_box = (new_box_x, new_box_y)
                new_person = (new_person_x, new_person_y)

                if isvalid(new_box_x, new_box_y) and isvalid(new_person_x, new_person_y) and check(person, new_person,
                                                                                                   box) and (
                new_box, new_person) not in visited:
                    visited.add((new_box, new_person))
                    q.append((dis + 1, new_box, new_person))
        return -1


# grid = [["#", "#", "#", "#", "#", "#"],
#         ["#", "T", "#", "#", "#", "#"],
#         ["#", ".", ".", "B", ".", "#"],
#         ["#", ".", "#", "#", ".", "#"],
#         ["#", ".", ".", ".", "S", "#"],
#         ["#", "#", "#", "#", "#", "#"]]

# grid = [["#", "#", "#", "#", "#", "#"],
#         ["#", "T", "#", "#", "#", "#"],
#         ["#", ".", ".", "B", ".", "#"],
#         ["#", "#", "#", "#", ".", "#"],
#         ["#", ".", ".", ".", "S", "#"],
#         ["#", "#", "#", "#", "#", "#"]]

# grid = [["#", "#", "#", "#", "#", "#", "#"],
#         ["#", "S", "#", ".", "B", "T", "#"],
#         ["#", "#", "#", "#", "#", "#", "#"]]

grid = [["#", ".", ".", "#", "#", "#", "#", "#"],
        ["#", ".", ".", "T", "#", ".", ".", "#"],
        ["#", ".", ".", ".", "#", "B", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", "#", ".", "S", "#"],
        ["#", ".", ".", "#", "#", "#", "#", "#"]]
s = Solution()
print(s.minPushBox(grid))
