import heapq
from collections import defaultdict
from typing import List


class Solution1:
    def __init__(self):
        self.path = set()

    def build_graph(self, edges):
        graph = defaultdict(list)

        for edge in edges:
            start = edge[0]
            to = edge[1]
            weight = edge[2]
            graph[start].append([to, weight])
            graph[to].append([start, weight])

        return graph

    def dfs(self, graph, node, distance, visited):
        # 当前节点记录进path
        self.path.add(node)
        # 当前节点记录进此时的路径
        visited.add(node)
        # 遍历邻居节点
        for nei in graph[node]:
            next_node, weight = nei[0], nei[1]
            # 超过距离，直接跳过
            if distance - weight < 0:
                continue
            # 之前访问过，直接跳过
            if next_node in visited:
                continue
            # 递归
            self.dfs(graph, next_node, distance - weight, visited)

        # 回溯，因为之后还可以从其它路径走到当前节点，并且可能是最短路径
        visited.remove(node)

        return

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        Time O(n^3)
        Space O(n)
        每个点用DFS的方式遍历所有路径，注意这里要记录到达的点是哪个，用来排查重复访问，同时离开一个点后需要回溯，因为还可以从其它路径走到此点。
        但是此方法明显超时TLE，因为有大量重复的访问节点，每一步并没有选择最短路径走。
        """
        graph = self.build_graph(edges)
        min_neighbors = float('inf')
        city = 0
        for i in range(n):
            # 记录是否访问过，用来避免走回头路
            visited = set()
            # 记录访问过的节点，避免重复计算访问过的节点
            self.path = set()
            self.dfs(graph, i, distanceThreshold, visited)
            # 更新最短距离和对应的邻居
            if len(self.path) <= min_neighbors:
                min_neighbors = len(self.path)
                city = i

        return city


class Solution2:
    def build_graph(self, edges):
        graph = defaultdict(list)

        for edge in edges:
            start = edge[0]
            to = edge[1]
            weight = edge[2]
            graph[start].append([to, weight])
            graph[to].append([start, weight])

        return graph

    def dijkstra(self, start, n, graph, distance_threshold):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重
        dist_to = [float('inf')] * n
        # base case，start 到 start 的最短距离就是 0
        dist_to[start] = 0

        # 优先级队列，dist_from_start 较小的排在前面
        pq = []
        # 从起点 start 开始进行 BFS
        heapq.heappush(pq, [start, 0])

        while pq:

            # 当前节点状态
            cur_state = heapq.heappop(pq)
            cur_node_id = cur_state[0]
            cur_dist_from_start = cur_state[1]

            # 如果需要找到起始点到某一个终点的最短路径和，在这里加一个判断就行了，其他代码不用改
            # if cur_node_id == end:
            #     return cur_dist_from_start

            # 如果已经有一条更短的路径到达 cur_node 节点了，不需要继续BFS遍历此节点，直接结束进下一个节点
            if cur_dist_from_start > dist_to[cur_node_id]:
                continue

            # 将 cur_node 的相邻节点装入队
            for neighbor in graph[cur_node_id]:

                # 下一个节点状态
                next_node_id = neighbor[0]
                # 看看从 cur_node 达到 next_node 的距离是否会更短
                dist_to_next_node = dist_to[cur_node_id] + neighbor[1]

                # 如果走到下一个节点的距离已经大于给定的现在的话，可以直接跳过
                if dist_to_next_node > distance_threshold:
                    continue

                # 如果有更短的走法，更新备忘录，同时加入优先级队列
                if dist_to_next_node < dist_to[next_node_id]:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, [next_node_id, dist_to_next_node])

        return dist_to

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        Time O(E + V * V * log(V))
        Space O(E + V)
        对每个节点能走到其它点的最短距离计算出来，然后计算最短距离是否在给定的范围内，如果是的就计算有多少个邻居，同时更新最少邻居的个数。
        """
        # 构建graph
        graph = self.build_graph(edges)
        min_neighbors = float('inf')
        city = 0
        for i in range(n):
            # 计算当前节点到其它点的最短距离
            dist_to = self.dijkstra(i, n, graph, distanceThreshold)
            neighbors = 0
            # 遍历所有距离
            for dist in dist_to:
                # 找到在给定范围内的距离
                if dist <= distanceThreshold:
                    # 计算邻居个数
                    neighbors += 1
            # 更新最少邻居个数和节点
            if neighbors <= min_neighbors:
                min_neighbors = neighbors
                city = i

        return city


s = Solution2()
print(s.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))
print(s.findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold=2))
print(s.findTheCity(n=6, edges=[[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]],
                    distanceThreshold=20))
