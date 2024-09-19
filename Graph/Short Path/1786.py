import heapq
from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            start = edge[0]
            end = edge[1]
            weight = edge[2]
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        return graph

    def dijkstra(self, n, graph):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重，注意这里是1开始的节点
        dist_to = [float('inf')] * (n + 1)
        # base case，start 到 start 的最短距离就是 0
        dist_to[n] = 0

        # 优先级队列，权重较小的排在前面
        pq = []
        heapq.heappush(pq, (0, n))

        while pq:
            # 当前节点状态
            cur_node = heapq.heappop(pq)
            cur_node_id = cur_node[1]
            cur_dist_from_start = cur_node[0]

            # 如果已经有一条更短的路径到达 cur_node 节点了，不需要继续BFS遍历此节点，直接结束进下一个节点
            if cur_dist_from_start > dist_to[cur_node_id]:
                continue

            # 将 cur_node 的相邻节点装入队
            for nei in graph[cur_node_id]:
                # 下一个节点状态
                next_node_id = nei[0]
                # 看看从 cur_node 达到 next_node 的距离是否会更短
                dist_to_next_node = dist_to[cur_node_id] + nei[1]

                # 如果有更短的走法，更新备忘录，同时加入优先级队列
                if dist_to_next_node < dist_to[next_node_id]:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_node_id))

        # 返回整个记录最短路径的数组
        return dist_to

    # def dfs(self, node, n, graph, dist_to, mod):
    #     暴力DFS写法，遍历所有合理的路径，TLE明显
    #     if node == n:
    #         self.count += 1
    #         self.count %= mod
    #         return
    #
    #     for nei in graph[node]:
    #         next_node_id = nei[0]
    #         if dist_to[next_node_id] >= dist_to[node]:
    #             continue
    #         self.dfs(next_node_id, n, graph, dist_to, mod)
    #
    #     return

    def dfs(self, node, n, graph, dist_to, mod, memo):
        # 走到终点了，找到一条合理的path
        if node == n:
            return 1

        # 访问过的节点，直接返回
        if memo[node] != -1:
            return memo[node]

        # 统计子节点的合理path个数
        sub = 0
        for nei in graph[node]:
            # 下一个节点
            next_node_id = nei[0]
            # 不符合题意的path，跳过
            if dist_to[next_node_id] >= dist_to[node]:
                continue
            # 叠加返回path的个数
            sub += self.dfs(next_node_id, n, graph, dist_to, mod, memo)
            # 注意要取余数
            sub %= mod

        # 记录进备忘录
        memo[node] = sub

        return memo[node]

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        """
        Time O(n + e * log(e) + n)
        Space O(n)
        先用dijkstra算出每个点到终点的最短路径，之后需要的是找出从起点1到终点n，总共有多少条符合题意的路径。这里可以直接暴力DFS找出所有路径，
        当然明显超时，也可以利用DP的思路，因为每个节点可以重复访问那么就会出现，当访问当前节点时候已经访问过了当前节点的所有后续的path，
        此时不在需要再次访问所有剩下的path，可以直接利用备忘录记录下来，返回path的个数。
        """
        # 需要返回余数
        mod = 10 ** 9 + 7
        # 构建图
        graph = self.build_graph(edges)

        # 计算到终点的最短路径，这里把终点最为起点
        dist_to = self.dijkstra(n, graph)

        # DFS带备忘录的DP写法，memo[i]记录走到当前节点有多少条合理的path
        memo = [-1] * (n + 1)
        res = self.dfs(1, n, graph, dist_to, mod, memo)

        return res


s = Solution()
print(s.countRestrictedPaths(n=5, edges=[[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]))
print(s.countRestrictedPaths(n=7, edges=[[1, 3, 1], [4, 1, 2], [7, 3, 4], [2, 5, 3], [5, 6, 1], [6, 7, 2], [7, 5, 3],
                                         [2, 6, 4]]))
