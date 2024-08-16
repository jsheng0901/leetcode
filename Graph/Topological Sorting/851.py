from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, n, richer):
        in_degree = [0] * n
        graph = defaultdict(list)
        for start, end in richer:
            graph[start].append(end)
            in_degree[end] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree, quiet):
        # 拓扑排序BFS模版
        queue = []
        # path[i]表示走到i这个节点的时候，最安静的值和最安静值对应的index
        path = [[quiet[i], i] for i in range(len(in_degree))]
        # 所有入度为0的先加入，作为起点
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        # 开始执行 BFS 算法
        while queue:
            cur = queue.pop(0)
            for nei in graph[cur]:
                # 对于邻居节点，如果邻居节点的安静值大于当前节点，那么我们就找到了，大于等于当前节点所有path上面节点中最安静的节点和值
                if path[cur][0] < path[nei][0]:
                    # 更新邻居节点对应的结果，注意这里一定要用path里面的当前节点值更新，因为path里面的结果是一直变动的
                    path[nei][0] = path[cur][0]
                    path[nei][1] = path[cur][1]
                in_degree[nei] -= 1
                # 如果入度为0，说明在拓扑排序路上
                if in_degree[nei] == 0:
                    queue.append(nei)

        return path

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        Time O(m + n)
        Space O(n)
        还是拓扑排序的思路，因为我们要找大于等于当前节点的所有节点里面最安静的那个，拓扑排序的过程就是构建最有钱到最穷的节点的过程，
        每一步记录走到当前节点的时候最安静的节点，注意这里不是记录全局当前最安静的节点，是path上面最安静的节点，否则会出现全局最安静的节点
        不一定能走到当前节点的情况。详细见注释。
        """
        # 构建图和入度数组
        n = len(quiet)
        graph, in_degree = self.build_graph(n, richer)

        # 计算走到每个节点的时候最安静的值和最安静的节点index
        path = self.bfs(graph, in_degree, quiet)
        # 拿出index作为结果
        res = [val[1] for val in path]
        return res


class Solution2:
    def build_graph(self, n, richer):
        in_degree = [0] * n
        graph = defaultdict(list)
        for start, end in richer:
            graph[start].append(end)
            in_degree[end] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree, quiet):
        # 拓扑排序BFS模版
        queue = []
        # path[i]表示走到i这个节点的时候，最安静值对应的index
        res = [i for i in range(len(in_degree))]
        # 所有入度为0的先加入，作为起点
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        # 开始执行 BFS 算法
        while queue:
            cur = queue.pop(0)
            for nei in graph[cur]:
                # 对于邻居节点，如果邻居节点的安静值大于当前节点，那么我们就找到了，大于等于当前节点所有path上面节点中最安静的节点
                # 注意这里是和思路1不一样的地方，实际上我们并不需要记录值，因为可以通过quiet数组找到值，只需要记录对应的index就行
                if quiet[res[cur]] < quiet[res[nei]]:
                    # 更新邻居节点对应的结果，注意这里一定要用res里面的当前节点值更新，因为res里面的结果是一直变动的
                    res[nei] = res[cur]
                in_degree[nei] -= 1
                # 如果入度为0，说明在拓扑排序路上
                if in_degree[nei] == 0:
                    queue.append(nei)

        return res

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        Time O(m + n)
        Space O(n)
        同思路1，区别在于我们并不需要记录最安静的值，我们只需要记录最安静的index，因为值可以随时从quiet里面拿到
        """
        # 构建图和入度数组
        n = len(quiet)
        graph, in_degree = self.build_graph(n, richer)

        # 计算走到每个节点的时候最安静的节点index
        res = self.bfs(graph, in_degree, quiet)
        return res


s = Solution2()
print(s.loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet=[3, 2, 5, 4, 6, 1, 7, 0]))
print(s.loudAndRich(richer=[[1, 2]], quiet=[0, 1, 2]))
