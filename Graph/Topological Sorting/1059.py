from collections import defaultdict
from typing import List


class Solution:
    def bfs(self, graph, in_degree, source, destination):
        # 拓扑排序BFS模版
        # 终点作为起点
        queue = [destination]

        while queue:
            cur = queue.pop(0)
            # 如果可以走到起点，说明所有path都在之间，没有环出现，直接返回true
            if cur == source:
                return True

            for nei in graph[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        # 如果不能走到起点，直接返回false
        return False

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Time O(e + v)
        Space O(e + v)
        拓扑排序的思路，但是此题重点是里面起点和终点的含义，如果反过来看，从终点可以按照拓扑排序走到起点，说明所有path都在起点和终点直接。
        如果有环，反过来从终点出发是不可能走到起点的。
        """
        # 构建拓扑排序的图
        in_degree = [0] * n
        graph = defaultdict(list)
        for edge in edges:
            start = edge[0]
            end = edge[1]
            # 如果终点有出度，说明不可能是终点，直接返回false
            if start == destination:
                return False
            graph[end].append(start)
            in_degree[start] += 1

        res = self.bfs(graph, in_degree, source, destination)

        return res


s = Solution()
print(s.leadsToDestination(n=3, edges=[[0, 1], [0, 2]], source=0, destination=2))
print(s.leadsToDestination(n=4, edges=[[0, 1], [0, 3], [1, 2], [2, 1]], source=0, destination=3))
print(s.leadsToDestination(n=4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]], source=0, destination=3))
