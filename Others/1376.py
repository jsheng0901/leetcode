from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        """
        O(n) time, O(n) space
        先记录所有上司: 下属的hash_map, bfs遍历所有节点 hash_map里面的key，记录时间
        """
        graph = defaultdict(set)

        for i, m in enumerate(manager):
            graph[m].add(i)

        queue = [(headID, 0)]
        res = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node, cur = queue.pop(0)
                if node in graph:
                    new = cur + informTime[node]
                    res = max(res, new)
                    for n in graph[node]:
                        queue.append((n, new))

        return res








