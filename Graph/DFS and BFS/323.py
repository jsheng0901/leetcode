from typing import List


class Solution:
    def dfs(self, node, seen, graph):
        seen[node] = True

        for nei in graph[node]:
            if seen[nei] is False:
                self.dfs(nei, seen, graph)

        return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Time O(E + V), E is length of edges for build graph, V is number of node for dfs visited
        Space O(E + V), E for build graph, V for dfs stack size
        almost same like 547, visited all connected nodes and each time visited mark as seen
        """
        count = 0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]
        # 构建无向图
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 遍历每个节点
        for i in range(n):
            # 如果没有访问过说明找到一个component
            if seen[i] is False:
                count += 1
                # 标记所有访问过的节点
                self.dfs(i, seen, graph)

        return count


s = Solution()
print(s.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))
print(s.countComponents(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
