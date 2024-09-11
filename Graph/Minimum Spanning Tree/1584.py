from typing import List


class Solution1:
    def distance(self, point1, point2):

        dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        return dist

    def prim(self, points, start):
        size = len(points)
        # dist[i]表示到i这个点最短的距离
        dist = [float('inf') for _ in range(size)]
        visit = set()
        # 起始位置到起始位置的边权值初始化为 0
        dist[start] = 0
        # 记录访问过的点
        visit.add(start)
        # 最小生成树的边权值
        mst = 0

        # 初始化一下，起始点到其它所有点的距离
        for i in range(1, size):
            dist[i] = self.distance(points[start], points[i])

        # 进行 n - 1 轮迭代，保证loop过每个点
        for _ in range(size - 1):
            # 记录当前轮最短距离和最短距离对应的另一个点
            min_dist = float('inf')
            min_dist_index = -1

            # 访问所有点，选择当前最小权重的点和权重
            for i in range(size):
                # 如果没有访问过，并且距离更短，记录最短距离和最短距离对应的点
                if i not in visit and dist[i] < min_dist:
                    min_dist = dist[i]
                    min_dist_index = i

            # 如果没有最短距离存在，返回 -1
            if min_dist_index == -1:
                return -1

            # 累加最短距离的权重
            mst += min_dist
            # 记录最访问过的点
            visit.add(min_dist_index)

            # 更新到每个点的最短距离权重，根据当前最小权重点
            for next_node in range(size):
                # 如果当前点没有被访问过
                if next_node not in visit:
                    # 此时最短距离可能是之前起始点到这个点的距离，也可能是新找到的最短距离对应的点到这个点的距离
                    dist[next_node] = min(dist[next_node], self.distance(points[min_dist_index], points[next_node]))

        return mst

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n + n) -> O(n)
        标准的prim写法的最小生成树的模版。
        """
        res = self.prim(points, 0)

        return res


class UnionFind:
    # 并查集的基础模版
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution2:
    def kruskal(self, edges, size):
        # 构建并查集
        union_find = UnionFind(size)

        # 将边按照权重从小到大排序
        edges.sort(key=lambda x: x[2])

        mst = 0
        for x, y, dist in edges:
            # 如果已经被连起来，则这条边会产生环，则不能加入 mst
            if union_find.is_connected(x, y):
                continue

            # 若这条边不会产生环，则属于最小生成树内的edge
            mst += dist
            # 连接这条边
            union_find.union(x, y)

        return mst

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Time O(n^2 + n^2 * log(n^2) + n^2 * alpha(n)) -> O(n^2 * log(n))
        Space O(n^2)
        最小生成树的kruskal模版写法。
        """
        # 先把所有的edge计算出来，并且存储起来
        size = len(points)
        edges = []
        for i in range(size):
            xi, yi = points[i]
            for j in range(i + 1, size):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                # 用坐标点在 points 中的索引表示坐标点
                edges.append([i, j, dist])

        ans = self.kruskal(edges, size)

        return ans


s = Solution2()
print(s.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(s.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
