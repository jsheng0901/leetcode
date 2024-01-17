from typing import List


class Solution1:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def bfs(self, grid, m, n, x, y):
        # BFS模板写到达所有build的最短距离
        visited = [[False] * n for _ in range(m)]
        queue = [(x, y)]
        visited[x][y] = True
        step = 0
        distance = 0
        num_builds = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                # 这里有个特殊的地方是，当我们到达build的时候，当前节点就不能再继续走了，所以要跳过当前节点
                if grid[x][y] == 1:
                    distance += step
                    num_builds += 1
                    continue
                for direction in self.directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if next_x >= m or next_x < 0 or next_y >= n or next_y < 0:
                        continue
                    if grid[next_x][next_y] == 2:
                        continue
                    if visited[next_x][next_y]:
                        continue
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
            step += 1

        return distance, num_builds

    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(n^2 * m^2)
        Space O(n * m)
        基本思想，对每个空的land都BFS一次到所有build的距离，然后找到可以到所有build的land中距离最短的。但很明显会超时。
        """
        m, n = len(grid), len(grid[0])
        results = []
        total_builds = 0
        # 遍历所有land可以到达build的最短距离
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    distance, num_builds = self.bfs(grid, m, n, x, y)
                    results.append((distance, num_builds))
                # 记录总共build的个数
                if grid[x][y] == 1:
                    total_builds += 1

        # check 可以到达所有 build 的 land 的最短距离
        min_dist = float('inf')
        for result in results:
            dist, builds = result[0], result[1]
            # 如果等于总build数量，则取最小值
            if builds == total_builds:
                min_dist = min(min_dist, dist)

        if min_dist == float('inf'):
            return -1
        else:
            return min_dist


class Solution2:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def bfs(self, grid, m, n, x, y, total_builds):
        visited = [[False] * n for _ in range(m)]
        queue = [(x, y)]
        visited[x][y] = True
        step = 0
        distance = 0
        num_builds = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                if grid[x][y] == 1:
                    distance += step
                    num_builds += 1
                    continue
                for direction in self.directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if next_x >= m or next_x < 0 or next_y >= n or next_y < 0:
                        continue
                    if grid[next_x][next_y] == 2:
                        continue
                    if visited[next_x][next_y]:
                        continue
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
            step += 1

        # 区别与思路1的地方在这里，当我们不能到达所有的build的时候，标记走过的所有land为2，减少后续不必要的遍历
        if num_builds != total_builds:
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 0 and visited[x][y]:
                        grid[x][y] == 2
            return float('inf')
        else:
            return distance

    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        Time O(n^2 * m^2)
        Space O(n * m)
        思路1的改良方法，当我们从一个land出发的时候不能到达所有的build，那说明这个land走过的所有路径里面的land都不可能到达所有build，
        此时我们可以把这些land标记成2，这样后面几不需要再遍历这些land了。不过此方法还是超时，因为如果都可以到达没有不能到达的land，那此方法
        和思路1没区别，这里我们从land的角度去找build，当build很多，land少的时候会更高效。
        """
        m, n = len(grid), len(grid[0])
        result = float('inf')
        total_builds = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    total_builds += 1

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    distance = self.bfs(grid, m, n, x, y, total_builds)
                    result = min(result, distance)

        return -1 if result == float('inf') else result


class Solution3:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def bfs(self, grid, x, y, m, n,  distance):
        # 同上一样的模板
        visited = [[False] * n for _ in range(m)]
        queue = [(x, y)]
        visited[x][y] = True
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                # 区别在这里，遇到land的时候更新一下两种状态
                if grid[x][y] == 0:
                    # 更新状态1，走到此land时用的距离
                    distance[x][y][0] += steps
                    # 更新状态2，多少个build可以走到这个land
                    distance[x][y][1] += 1

                for direction in self.directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if next_x >= m or next_x < 0 or next_y >= n or next_y < 0:
                        continue
                    if grid[next_x][next_y] == 2 or grid[next_x][next_y] == 1:
                        continue
                    if visited[next_x][next_y]:
                        continue
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
            steps += 1

        return distance

    def shortestDistance(self, grid: [[int]]) -> int:
        """
        Time O(n^2 * m^2)
        Space O(n * m)
        和上面的思路不一样的是，这里我们从build的角度找land，当build少land多的时候更高效，减少多余的遍历。此思路不会超时。
        我们需要一个数组去存储每个land的两种状态，此时我们需要一个三维记录每个land的上面两种状态。
            1. 从每个build走到此land的时候总共花费了多少steps
            2. 总共有多少个build可以reach这个land。
        """
        m, n = len(grid), len(grid[0])
        total_house = 0
        min_distance = float('inf')
        # 记录每个land的两种状态，用双loop不要用 *len(grid[0])
        distance = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    # 如果是build，那么记录总共的build个数，和标记land的状态
                    total_house += 1
                    self.bfs(grid, x, y, m, n,  distance)

        # 对所有land进行遍历，如果可以到达所有build，去distance最小值即可
        for x in range(m):
            for y in range(n):
                if distance[x][y][1] == total_house:
                    min_distance = min(min_distance, distance[x][y][0])

        return -1 if min_distance == float('inf') else min_distance


class Solution4:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def bfs(self, grid, x, y, m, n,  distance, empty_land_value, min_distance):
        queue = [(x, y)]
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                # 区别在这里，遇到land的时候，我们需要记录此时的距离和同时更新走到这个land的最短距离
                # 这里不需要记录有多少个build可以走到这里，因为我们用 empty_land_value 控制了能走到此land的说明之前的build都可走到
                # 这里check值等于当前BFS的land的访问值 - 1，因为我们在加入此节点的时候就标记了 -1，所以不能用当前的land值
                if grid[x][y] == empty_land_value - 1:
                    distance[x][y] += steps
                    min_distance = min(min_distance, distance[x][y])

                for direction in self.directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]

                    if next_x >= m or next_x < 0 or next_y >= n or next_y < 0:
                        continue
                    # 这里只需要判断是否是之前走到过的land就可以，其它值一律不能走到
                    # 防止走回路，在同一个BFS里面，之前走过land再加入queue后的已经被 -1 了，所以不会等于 empty_land_value
                    if grid[next_x][next_y] != empty_land_value:
                        continue
                    # 加入下一个访问节点
                    queue.append((next_x, next_y))
                    # 这里一定要标记一下，下一个要访问的节点的值要 -1
                    grid[next_x][next_y] -= 1
            steps += 1

        return min_distance

    def shortestDistance(self, grid: [[int]]) -> int:
        """
        Time O(n^2 * m^2)
        Space O(n * m)
        核实思路和思路3一模一样，但是我们可以避免多次重复访问land，这里我们用一个 mark 去标记访问过的land，每次BFS我们不需要访问之前没走过
        的land，因为之前build走不到的land说明一定不可能到达所有build，所以每次BFS访问land的时候我们更新一下 mark，然后下一次只访问上一此
        走过的land。可以有效减少访问不会走到所有building的land。同时这里也不再需要visited数组记录访问过，因为我们只会访问land的value，
        也不需要两个状态，因为能走到的land一定是之前都走过的，也就是所有building都能走到的。
        """
        m, n = len(grid), len(grid[0])
        min_distance = float('inf')
        # 记录到达每个节点的距离和
        distance = [[0] * n for _ in range(m)]
        # 初始值land表示land被放过的value
        empty_land_value = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    # 每次BFS前要初始化，不然下一个build拿的是上一个build到达land的最小值去比较
                    min_distance = float('inf')
                    min_distance = self.bfs(grid, x, y, m, n, distance, empty_land_value, min_distance)
                    # 更新下一个land访问值
                    empty_land_value -= 1

        return -1 if min_distance == float('inf') else min_distance


s = Solution4()
print(s.shortestDistance(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
print(s.shortestDistance(
    [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
     [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]))
