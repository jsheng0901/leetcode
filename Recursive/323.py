class Solution:
    def countComponents(self, n: int, edges: [[int]]) -> int:
        """
        O(E + V) time, E is length of edges for build graph, V is number of node for dfs visited
        O(E + V) space E for build graph, V for dfs stack size
        almost same like 547, visited all connected nodes and each time visited mark as seen
        """
        count = 0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for adj in graph[node]:
                if seen[adj] is False:
                    seen[adj] = True
                    dfs(adj)

        for i in range(n):
            if seen[i] is False:
                count += 1
                seen[i] = True
                dfs(i)

        return count
