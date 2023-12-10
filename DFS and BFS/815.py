from collections import defaultdict
from typing import List


class Solution:
    def bfs(self, graph, source, target, routes):
        # 初始化列队和visited数组，防止访问重复的route
        queue = []
        visited = set()
        # 初始化所有可能的route
        for route in graph[source]:
            queue.append(route)
            visited.add(route)
        # 计数
        bus = 1
        while queue:
            size = len(queue)
            # 遍历router下所有stop
            for _ in range(size):
                # 当前遍历到的route
                top = queue.pop(0)
                # 遍历此route下面所有的stop
                for stop in routes[top]:
                    # 如果走到终点，直接返回公交车数量
                    if stop == target:
                        return bus
                    # 对于所有此stop可以访问route，没有访问过的进入列队
                    for next_route in graph[stop]:
                        if next_route not in visited:
                            queue.append(next_route)
                            visited.add(next_route)
            bus += 1
        return -1

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        Time O(m * k * m)   m: number of routes, k: max number of stops in one route
        Space O(m * k * m)
        此题构建graph比较巧妙，用stop当节点，统计每站可以到的路线，再对于每个站我们遍历这个站可以去到的路线，
        对于每个路线我们再遍历可以到的所有站。每个路线只能走一次，不走重复路线。直到遇到终点。每次换路线我们统计坐过的公交车数量。
        """
        # 特殊情况，起点终点一样，直接返回0
        if source == target:
            return 0

        graph = defaultdict(list)
        # 构建图，节点是stop，链接的是stop对应的route的index
        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                graph[stop].append(i)

        return self.bfs(graph, source, target, routes)


s = Solution()
print(s.numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6))
