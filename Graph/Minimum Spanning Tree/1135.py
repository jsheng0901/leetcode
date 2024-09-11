from typing import List


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


class Solution:
    def kruskal(self, connections, n):
        # 城市编号为 1...n，所以初始化大小为 n + 1
        union_find = UnionFind(n + 1)

        # 对所有边按照权重从小到大排序
        connections.sort(key=lambda x: x[2])

        # 记录最小生成树的权重之和
        mst = 0

        for edge in connections:
            u, v, weight = edge
            # 若这条边会产生环，则不能加入 mst
            if union_find.is_connected(u, v):
                continue

            # 若这条边不会产生环，则属于最小生成树
            mst += weight
            union_find.union(u, v)

        # 保证所有节点都被连通
        # 按理说 uf.count() == 1 说明所有节点被连通
        # 但因为节点 0 没有被使用，所以 0 会额外占用一个连通分量
        return mst if union_find.count == 2 else -1

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        Time O(n^2 + n^2 * log(n^2) + n^2 * alpha(n)) -> O(n^2 * log(n))
        Space O(n)
        最小生成树的kruskal模版题。
        """
        res = self.kruskal(connections, n)

        return res


s = Solution()
print(s.minimumCost(n=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
print(s.minimumCost(n=4, connections=[[1, 2, 3], [3, 4, 4]]))
