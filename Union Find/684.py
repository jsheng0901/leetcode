from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

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

    def connected(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        return root_x == root_y


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        并查集模板题，把所有edge连接起来，然后check出发地和目的地是否链接，如果连接过说明是多余的边需要被删除，
        如果没有链接说明是新的边直接连起来。
        """

        uf = UnionFind(len(edges))
        redundant_edge = None

        for edge in edges:
            # 注意这里需要把index转化一下，因为edge是1开始，而UF是0开始
            node1, node2 = edge[0] - 1, edge[1] - 1
            if uf.connected(node1, node2):
                redundant_edge = edge
            else:
                uf.union(node1, node2)

        return redundant_edge
