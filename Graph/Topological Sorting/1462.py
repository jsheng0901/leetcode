from collections import defaultdict
from typing import List, Any


class Solution1:
    def build_graph(self, numCourses: int, prerequisites: List[List[int]]) -> list[list[Any]]:
        # 建图函数
        # 图中共有 numCourses 个节点
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            from_course, to_course = edge[0], edge[1]
            # 修完课程 from 才能修课程 to
            # 在图中添加一条从 from 指向 to 的有向边
            graph[from_course].append(to_course)

        return graph

    def bfs(self, query, graph):
        # 需要query的起点和终点
        start, end = query[0], query[1]
        # 初始化列队
        q = [start]
        visited = set()
        visited.add(start)

        while q:
            cur = q.pop(0)
            # 走到终点，直接返回true
            if cur == end:
                return True

            for next_course in graph[cur]:
                if next_course not in visited:
                    q.append(next_course)
                    visited.add(next_course)
        # 走不到终点，返回false
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> (
            List)[bool]:
        """
        Time O(q * n)
        Space O(n)
        暴力法，直接对每个query的起点和终点进行BFS搜索，走的到就是true，走不到就是false，就是每次query都可能需要遍历整个graph
        """
        graph = self.build_graph(numCourses, prerequisites)

        ans = []
        # 遍历所有query
        for query in queries:
            ans.append(self.bfs(query, graph))

        return ans


class Solution2:
    def build_graph(self, numCourses: int, prerequisites: List[List[int]]) -> tuple[list[list[Any]], list[int]]:
        # 建图函数
        # 图中共有 numCourses 个节点
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for edge in prerequisites:
            from_course, to_course = edge[0], edge[1]
            # 修完课程 from 才能修课程 to
            # 在图中添加一条从 from 指向 to 的有向边
            graph[from_course].append(to_course)
            in_degree[to_course] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree, numCourses):
        # 根据入度初始化队列中的节点
        q = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        # 记录拓扑排序每个节点的路径结果，也就是每个节点的所有父节点
        # 这里用set，保证节约内存，否则会有很多重复的节点在父节点里面，同时查存的时候会很慢
        topological_sort = defaultdict(set)
        # 开始执行 BFS 算法
        while q:
            cur = q.pop(0)
            # 弹出节点的顺序即为拓扑排序结果
            for next_course in graph[cur]:
                # 邻居节点的父节点添加当前节点
                topological_sort[next_course].add(cur)
                # 邻居节点的父节点添加当前节点的所有父节点
                topological_sort[next_course].update(topological_sort[cur])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)

        return topological_sort

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> (
            List)[bool]:
        """
        Time O(n + q)
        Space O(n)
        其实我们并不需要每次都遍历整个graph，完全可以按照拓扑排序的思路遍历一次graph，记录上每个节点之前的所有父节点，此时query的时候
        我们只需要查一下起点节点是否在我们的终点节点的拓扑排序的路径上面即可。记录每个节点拓扑排序的父节点用字典和set，保证快速查找和节约内存。
        """
        # 构件图和入度数组
        graph, in_degree = self.build_graph(numCourses, prerequisites)
        # 遍历一次图，记录所有节点拓扑排序的父节点
        topological_sort = self.bfs(graph, in_degree, numCourses)

        ans = []
        # 遍历所有query
        for query in queries:
            from_course, to_course = query[0], query[1]
            # 查找起点节点是否在终点节点的拓扑排序的路径上面
            ans.append(from_course in topological_sort[to_course])

        return ans


s = Solution2()
print(s.checkIfPrerequisite(numCourses=2, prerequisites=[], queries=[[1, 0], [0, 1]]))
print(s.checkIfPrerequisite(numCourses=4, prerequisites=[[2, 3], [2, 1], [0, 3], [0, 1]],
                            queries=[[0, 1], [0, 3], [2, 3], [3, 0], [2, 0], [0, 2]]))
print(s.checkIfPrerequisite(numCourses=7, prerequisites=[[2, 3], [2, 1], [0, 3], [0, 1]],
                            queries=[[0, 1], [0, 3], [2, 3], [3, 0], [2, 0], [0, 2]]))
print(s.checkIfPrerequisite(numCourses=7,
                            prerequisites=[[2, 3], [2, 1], [2, 0], [3, 4], [3, 6], [5, 1], [5, 0], [1, 4], [1, 0],
                                           [4, 0], [0, 6]],
                            queries=[[3, 0], [6, 4], [5, 6], [2, 6], [2, 3], [5, 6], [4, 0], [2, 6], [3, 5], [5, 3],
                                     [1, 6], [1, 0], [3, 5], [6, 5], [2, 3], [3, 0], [3, 4], [3, 4], [2, 5], [0, 3],
                                     [4, 0], [6, 4], [5, 0], [6, 5], [5, 6], [6, 5], [1, 0], [3, 4], [1, 5], [1, 4],
                                     [3, 6], [0, 1], [1, 2], [5, 1], [5, 3], [5, 3], [3, 4], [5, 4], [5, 4], [5, 3]]))
