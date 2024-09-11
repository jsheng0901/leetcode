import heapq
from collections import defaultdict
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


class Solution1:
    def kruskal(self, edges, n):
        # 节点编号为 1...n，所以初始化大小为 n + 1
        union_find = UnionFind(n + 1)

        # 对所有边按照权重从小到大排序
        edges.sort(key=lambda x: x[2])

        # 记录最小生成树的权重之和
        mst = 0

        for edge in edges:
            u, v, weight = edge
            # 若这条边会产生环，则不能加入 mst
            if union_find.is_connected(u, v):
                continue

            # 若这条边不会产生环，则属于最小生成树
            mst += weight
            union_find.union(u, v)

        return mst

    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        Time O(n + m * log(m) + m * alpha(m)) -> O(m * log(m))  m -> number of edges after add virtual node edge
        Space O(m)
        此题有一个很trick的地方是，如何在graph里面表示在当前节点打well的权重，我们可以用一个virtual节点，此节点到其它所有节点的权重为
        每个节点的建well的权重值，这样就变成了一个简单的MST问题，用kruskal模版即可。
        """
        # 加入每个节点到虚拟节点的边，权重为建well的cost
        virtual_node = 0
        # 注意这里index从1开始
        for i, val in enumerate(wells, 1):
            pipes.append([virtual_node, i, val])

        mst = self.kruskal(pipes, n)

        return mst


class Solution2:
    def prim(self, graph, n):
        # A set to maintain all the vertex that has been added to
        #   the final MST (Minimum Spanning Tree),
        #   starting from the vertex 0.
        mst_set = {0}

        # heap to maintain the order of edges to be visited,
        #   starting from the edges originated from the vertex 0.
        # Note: we can start arbitrarily from any node.
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        mst = 0
        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                # adding the new vertex into the set
                mst_set.add(next_house)
                mst += cost
                # expanding the candidates of edge to choose from
                #   in the next round
                for new_cost, neighbor_house in graph[next_house]:
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbor_house))

        return mst

    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        Time O((n + m) * log(n + m))    n -> number of node     m -> number of edge
        Space O(n + m)
        同思路1，换成prim的MST模版写，这里prim是原始版本没有优化过的。
        """
        # bidirectional graph represented in adjacency list
        graph = defaultdict(list)

        # add a virtual vertex indexed with 0.
        #   then add an edge to each of the house weighted by the cost
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))

        # add the bidirectional edges to the graph
        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))

        total_cost = self.prim(graph, n)

        return total_cost


s = Solution1()
print(s.minCostToSupplyWater(n=5, wells=[46012, 72474, 64965, 751, 33304],
                             pipes=[[2, 1, 6719], [3, 2, 75312], [5, 3, 44918]]))
