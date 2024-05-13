from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.number_nodes = 0

    def build_graph(self, edges):
        graph = defaultdict(list)

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        return graph

    def dfs(self, node, graph, visited):

        # 标准DFS框架，计算访问node的个数
        visited[node] = True
        self.number_nodes += 1
        for nei in graph[node]:
            if visited[nei] is False:
                self.dfs(nei, graph, visited)

        return

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        Time O(n + e)
        Space O(n)
        先构建graph，通过数学高斯数列计算如果全都链接有多少个edges，然后再通过DFS遍历所有component，记录每个component里面node的个数，
        同理计算总共的edges，计算出所有component可以构成的edges。最后相减就是不能reach的pair edges。
        """
        # 如果都链接可以构成多少edges
        total_pairs = (n - 1 + 1) * (n - 1) / 2
        # 构建无向图graph
        graph = self.build_graph(edges)
        # 防止访问重复node
        visited = [False] * n
        # 记录可以到达的edges
        reached_pairs = 0

        for i in range(n):
            if visited[i] is False:
                # 每次初始化这个component包含的nodes
                self.number_nodes = 0
                # DFS遍历此component
                self.dfs(i, graph, visited)
                # 计算多少个可以reach的edges在这个component里面
                reached_pairs += (self.number_nodes - 1 + 1) * (self.number_nodes - 1) / 2

        # 相减得出不能reach的edges个数
        return int(total_pairs - reached_pairs)


s = Solution()
print(s.countPairs(n=3, edges=[[0, 1], [0, 2], [1, 2]]))
print(s.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
