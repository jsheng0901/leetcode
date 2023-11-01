from collections import defaultdict
from typing import List


class Solution:
    def tarjin(self, graph, dfn, low, time, cur, pre, ans):
        dfn[cur] = time
        low[cur] = time

        for nei in graph[cur]:
            if nei == pre:
                continue

            if dfn[nei] == 0:
                self.tarjin(graph, dfn, low, time + 1, nei, cur, ans)
                low[cur] = min(low[cur], low[nei])
                if low[nei] > dfn[cur]:
                    ans.append([cur, nei])
            else:
                low[cur] = min(low[cur], low[nei])

        return

    def build_graph(self, connections):
        graph = defaultdict(list)
        for connection in connections:
            node1, node2 = connection[0], connection[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        return graph

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Time O(n)
        Space O(n)
        tarjin 算法的变形应用。
        """
        graph = self.build_graph(connections)
        dfn = [0] * n
        low = [0] * n
        time = 1
        ans = []

        self.tarjin(graph, dfn, low, time, 0, -1, ans)

        return ans

