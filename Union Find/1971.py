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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Time O(n)
        Space O(n)
        并查集模板题，把所有edge连接起来，然后check出发地和目的地是否链接。
        """
        uf = UnionFind(n)

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            uf.union(node1, node2)

        return uf.connected(source, destination)
