from collections import defaultdict
from typing import List


class Solution1:
    def build_graph(self, edges):

        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        return graph

    def dfs(self, node, graph, seen):

        # 记录当前节点
        seen.add(node)
        # 遍历邻居节点
        for nei in graph[node]:
            # 访问过，跳过
            if nei in seen:
                continue
            self.dfs(nei, graph, seen)

        return

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time O(n)
        space O(n)
        很简单的查图是否有环并且全部连起来的DFS写法。详细见注释
        """
        # 确保没有环，如果一个图所有edge都连起来并且没有环，那么一定满足以下公式
        if len(edges) != n - 1:
            return False

        # 构建图
        graph = self.build_graph(edges)

        # 记录访问过的点，保证不走回头路
        seen = set()

        # DFS遍历所有节点
        self.dfs(0, graph, seen)

        # 判断是否访问过的节点等于所有节点个数，如果不相等，说明有的节点没有相连接起来
        return len(seen) == n


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count -= 1

    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        return root_x == root_y


class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time O(n * alpha(n))
        Space O(n)
        并查集的思路，判断分桶个数，全部连起来的话应该只有一个分桶。
        """
        uf = UnionFind(n)

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            # 如果已经连接起来过，说明有环
            if uf.connected(node1, node2):
                return False
            # 链接起来两个节点
            uf.union(node1, node2)

        # 判断分桶个数是否只有一个
        return uf.count == 1


s = Solution1()
print(s.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
