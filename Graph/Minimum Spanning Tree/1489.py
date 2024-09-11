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

    def kruskal(self, edges, uf, init_mst):
        # 记录最小生成树的权重之和
        mst = init_mst

        for edge in edges:
            u, v, weight, _ = edge
            # 若这条边会产生环，则不能加入 mst
            if uf.is_connected(u, v):
                continue

            # 若这条边不会产生环，则属于最小生成树
            mst += weight
            uf.union(u, v)

        return mst, uf.count

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Time O(m + m * log(m) + m * (m * alpha(n))) -> O(m^2 * alpha(n))
        Space O(m)
        此题很直接，先构建MST计算出正常情况下的权重，
        对于critical edge，我们忽略这个edge，然后再构建一次MST，如果权重更大或者多余1个component，那么说明这个被忽略的edge是critical。
        对于pseudo critical edge，同样我们先force这个edge相连接再UF里面，然后计算一次MST，如果权重一样，说明此edge是pseudo critical。
        """
        # 添加原始的index，因为后面要重新排序，方便后续直接记录原始index进结果
        for i, edge in enumerate(edges):
            edge.append(i)

        # 对所有边按照权重从小到大排序
        edges.sort(key=lambda x: x[2])

        # 计算标准状态下的MST权重
        uf = UnionFind(n)
        mst_weight, _ = self.kruskal(edges, uf, 0)

        critical = []
        pseudo_critical = []
        # 检查每一条边 for critical and pseudo-critical
        for i in range(len(edges)):
            # 删除当前edge后行的edges
            new_edges = edges[:i] + edges[i + 1:]

            # 计算忽略的情况下的MST
            uf_ignore = UnionFind(n)
            mst_ignore_weight, new_count = self.kruskal(new_edges, uf_ignore, 0)
            # 如果大于一个component或者权重更大，说明是critical
            if new_count > 1 or mst_ignore_weight > mst_weight:
                critical.append(edges[i][3])
                continue

            # 计算force这条边相连接的情况下的MST
            uf_force = UnionFind(n)
            # 初始值权重为当前这条边的权重
            init_mst = edges[i][2]
            # force相连接这条边
            uf_force.union(edges[i][0], edges[i][1])
            mst_force_weight, _ = self.kruskal(new_edges, uf_force, init_mst)
            # 如果权重没有变化，说明是pseudo critical
            if mst_force_weight == mst_weight:
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]


s = Solution()
print(s.findCriticalAndPseudoCriticalEdges(n=6, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 4], [3, 4, 2], [3, 5, 2],
                                                       [4, 5, 2]]))
