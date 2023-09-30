from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.valid = False

    def dfs(self, graph, node, destination, visited):

        if node == destination:
            self.valid = True
            return

        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                self.dfs(graph, nei, destination, visited)

        return

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Time O(n)
        Space O(n)
        DFS写法，走遍整graph，如果到达目的地，则全局参数记录true，否则false。
        """
        graph = defaultdict(list)
        visited = set()

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        self.dfs(graph, source, destination, visited)

        return self.valid


s = Solution()
print(
    s.validPath(n=10,
                edges=[[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
                source=5,
                destination=9)
)
