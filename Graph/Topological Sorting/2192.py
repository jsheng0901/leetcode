from collections import defaultdict
from typing import List, Any


class Solution1:
    def build_graph(self, n: int, edges: List[List[int]]) -> tuple[list[list[Any]], list[int]]:
        # 建图函数
        # 图中共有 n 个节点
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for edge in edges:
            start, end = edge[0], edge[1]
            # 在图中添加一条从 start 指向 end 的有向边
            graph[start].append(end)
            in_degree[end] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree):
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
            for nei in graph[cur]:
                # 邻居节点的父节点添加当前节点
                topological_sort[nei].add(cur)
                # 邻居节点的父节点添加当前节点的所有父节点
                topological_sort[nei].update(topological_sort[cur])
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return topological_sort

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Time O(n^2 + m)     worse case graph is chain, last part create ancestors list take n^2
        Space O(n^2 + m)
        此题和1462几乎是一模一样的思路，拓扑排序，同时记录每个节点的所有先祖节点。不同的地方在于，最后要对每个节点的先祖节点进行排序，
        这里使用双loop的写法，最差情况可能是O(n^2)。
        """
        # 构建图
        graph, in_degree = self.build_graph(n, edges)
        # 拓扑排序拿到每个节点的所有先祖节点
        topological_sort = self.bfs(graph, in_degree)
        # 对所有节点的先祖节点进行排序
        ancestors_list = [[] for _ in range(n)]
        for i in range(n):
            for node in range(n):
                if node == i:
                    continue
                if node in topological_sort[i]:
                    ancestors_list[i].append(node)

        return ancestors_list


class Solution2:
    def build_graph(self, n: int, edges: List[List[int]]) -> tuple[list[list[Any]], list[int]]:
        # 建图函数
        # 图中共有 n 个节点
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for edge in edges:
            start, end = edge[0], edge[1]
            # 在图中添加一条从 start 指向 end 的有向边
            graph[start].append(end)
            in_degree[end] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree):
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
            for nei in graph[cur]:
                # 邻居节点的父节点添加当前节点
                topological_sort[nei].add(cur)
                # 邻居节点的父节点添加当前节点的所有父节点
                topological_sort[nei].update(topological_sort[cur])
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return topological_sort

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        Time O(n + m + n * n * log(n))     worse case graph is chain, last part create ancestors list take n^2 * log(n)
        Space O(n^2 + m)
        和思路1一模一样，只是最后的排序换成直接对每个节点的先祖节点sort，虽然每个节点需要O(n * log(n))的时间进行排序，
        但是其实最差情况每个节点的先祖节点个数应该是从0到n-1递增的个数，当节点不是很多的时候，理论上其实更快对比思路1。
        """
        graph, in_degree = self.build_graph(n, edges)

        topological_sort = self.bfs(graph, in_degree)

        # 直接对set里面的先祖节点进行排序
        ans = []
        for i in range(n):
            ans.append(sorted(list(topological_sort[i])))

        return ans


s = Solution2()
print(s.getAncestors(n=8, edges=[[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
print(s.getAncestors(n=5, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
