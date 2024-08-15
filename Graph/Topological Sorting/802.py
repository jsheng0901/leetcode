from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, graph):
        # 反向构建图
        reverse_graph = defaultdict(list)
        in_degree = [0] * len(graph)

        for i in range(len(graph)):
            for node in graph[i]:
                reverse_graph[node].append(i)
                in_degree[i] += 1

        return reverse_graph, in_degree

    def bfs(self, graph, in_degree):
        # 拓扑排序BFS模版
        queue = []
        # 所有入度为0的先加入，作为起点
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        # 记录拓扑排序结果
        res = []
        # 开始执行 BFS 算法
        while queue:
            cur = queue.pop(0)
            # 弹出节点的顺序即为拓扑排序结果，这里因为后续需要reverse结果，所以我们不在这里记录拓扑节点，否则需要sort结果，增加复杂度。
            # res.append(cur)
            for nei in graph[cur]:
                in_degree[nei] -= 1
                # 如果入度为0，说明在拓扑排序路上
                if in_degree[nei] == 0:
                    queue.append(nei)

        # 在这里进行加入所有节点，保证加入节点的顺序是从小到大的顺序
        for i, val in enumerate(in_degree):
            # 入度为0说明在之前的拓扑排序路上
            if val == 0:
                res.append(i)

        return res

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Time O(m + n)
        Space O(m + n)
        此题是拓扑排序改版，终点节点应该是拓扑排序里面的起点，没有入度。对应的安全节点应该是拓扑排序后整个排序结果上的所有点。
        只需要反过来构建图然后再拓扑排序一下，拿到所有排序过后节点即可。也就是在环里面的节点不会被拿出来。
        需要注意的是，最后要变回之前的graph，需要reverse一下。
        """
        # 反向构建图，得到入度的数组
        reverse_graph, in_degree = self.build_graph(graph)

        # BFS版本拓扑排序
        res = self.bfs(reverse_graph, in_degree)

        return res


s = Solution()
print(s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
