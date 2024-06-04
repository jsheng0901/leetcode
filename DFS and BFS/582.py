from collections import defaultdict
from typing import List


class Solution1:
    def dfs(self, graph, node, path):

        path.append(node)
        for child in graph[node]:
            self.dfs(graph, child, path)

        return

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        Time O(n)
        Space O(n)
        构建有向图，然后DFS遍历已kill为起点的所有子节点，并加入path。
        """
        graph = defaultdict(list)
        for parent, child in zip(ppid, pid):
            graph[parent].append(child)

        path = []
        self.dfs(graph, kill, path)

        return path


class Solution2:
    def bfs(self, graph, start):

        queue = [start]
        path = []

        while queue:
            top = queue.pop(0)
            path.append(top)
            for child in graph[top]:
                if child:
                    queue.append(child)

        return path

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        Time O(n)
        Space O(n)
        构建有向图，然后BFS遍历已kill为起点的所有子节点，并加入path。
        """
        graph = defaultdict(list)
        for parent, child in zip(ppid, pid):
            graph[parent].append(child)

        path = self.bfs(graph, kill)

        return path


s = Solution1()
print(s.killProcess(pid=[1, 3, 10, 5], ppid=[3, 0, 5, 3], kill=5))
