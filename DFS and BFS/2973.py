from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.coins = []

    def build_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            source, target = edge[0], edge[1]
            graph[source].append(target)
            graph[target].append(source)

        return graph

    def traversal(self, graph, cost, node, visited):
        # 这里可以不加判断，因为叶子结点不会走回头路，并且就当前节点一个结果直接返回sub，并且后续if判断赋值

        # 当前节点先记录下来
        sub = [cost[node]]
        # 记录当前节点访问过
        visited[node] = True
        # 遍历邻居节点
        for nei in graph[node]:
            # 没有访问过进递归
            if visited[nei] is False:
                # 记录返回值进sub
                sub.extend(self.traversal(graph, cost, nei, visited))

        # 如果小于3，赋值1
        if len(sub) < 3:
            self.coins[node] = 1
        else:
            # 否者，先sort，从小打到
            sub.sort()
            # 找到最大的三个数乘积
            max_product = max(0, sub[-1] * max(sub[0] * sub[1], sub[-3] * sub[-2]))
            # 赋值
            self.coins[node] = max_product

        # 返回list
        return sub

    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        """
        Time O(n * n * log(n))
        Space O(n + n^2)
        遍历每个节点，每个节点都按照树的后续遍历方法，拿到所有返回值，并且sort存储起来。然后找到sort后最大的三个乘积。
        这里最大的三个乘积分别可以是最小的两个数*最大的数或者最大的三个数，因为可能可以最小的两个数是负数，相乘后大于零。
        这里耗时的是每次都要sort一遍所有返回值，其实应该是不需要每次都sort整个list的，可以找个办法如何快速merge两个sort过的list。
        """
        # 记录结果
        self.coins = [0] * len(cost)
        # 构建双向图
        graph = self.build_graph(edges)
        # 防止走回头路
        visited = [False] * len(cost)
        # 遍历树，其实这里是DFS后序遍历图
        self.traversal(graph, cost, 0, visited)

        return self.coins


s1 = Solution()
print(s1.placedCoins(edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], cost=[1, 2, 3, 4, 5, 6]))
s2 = Solution()
print(s2.placedCoins(edges=
                     [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]],
                     cost=[1, 4, 2, 3, 5, 7, 8, -4, 2]))
s3 = Solution()
print(s3.placedCoins(edges=[[0, 1], [0, 2]], cost=[1, 2, -2]))
