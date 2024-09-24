import heapq
from collections import defaultdict
from functools import cache
from typing import List


class Solution1:
    def build_graph(self, roads):
        graph = defaultdict(list)
        for road in roads:
            start = road[0]
            end = road[1]
            weight = road[2]
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        return graph

    def dijkstra(self, n, graph):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重
        dist_to = [float('inf')] * n
        # base case，start 到 start 的最短距离就是 0
        dist_to[0] = 0

        # 优先级队列，权重较小的排在前面
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq:
            # 当前节点状态
            cur_node = heapq.heappop(pq)
            cur_node_id = cur_node[1]
            cur_dist_from_start = cur_node[0]

            # 走到终点，直接返回距离
            if cur_node_id == n - 1:
                return cur_dist_from_start

            # 如果已经有一条更短的路径到达 cur_node 节点了，不需要继续BFS遍历此节点，直接结束进下一个节点
            if cur_dist_from_start > dist_to[cur_node_id]:
                continue

            # 将 cur_node 的相邻节点装入队
            for nei in graph[cur_node_id]:
                # 下一个节点状态
                next_node_id = nei[0]
                # 看看从 cur_node 达到 next_node 的距离是否会更短
                dist_to_next_node = cur_dist_from_start + nei[1]

                # 如果有更短的走法，更新备忘录，同时加入优先级队列
                if dist_to_next_node < dist_to[next_node_id]:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_node_id))

        return -1

    def dp(self, node, n, graph, total_time, memo, mod):
        # 走到终点了，找到一条合理的路径
        if node == n - 1:
            return 1

        # 之前走过，返回备忘录结果
        if memo[node][total_time] != -1:
            return memo[node][total_time]

        # 统计子节点的结果
        sub = 0
        for nei in graph[node]:
            next_node_id = nei[0]
            time = nei[1]
            # 走不通的路径，跳过
            if total_time - time < 0:
                continue
            # 累加子节点返回值
            sub += self.dp(next_node_id, n, graph, total_time - time, memo, mod)
            sub %= mod

        # 存入备忘录
        memo[node][total_time] = sub

        return memo[node][total_time]

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Time O(e + e * log(e) + t * n)
        Space O(n * t)
        同理1786的思路，先找到最短路径，再进行DP的思路找到符合条件的所有路径个数。这里直接写最直接的DP版本，但是会TLE。详细见注释。
        """
        mod = 10 ** 9 + 7
        # 构件图
        graph = self.build_graph(roads)
        # 找到最短距离
        shortest_time = self.dijkstra(n, graph)

        # 构建DP的备忘录
        memo = [[-1] * (shortest_time + 1) for _ in range(n)]
        # 带备忘录的DFS就是DP
        res = self.dp(0, n, graph, shortest_time, memo, mod)

        return res


class Solution2:
    def build_graph(self, roads):
        graph = defaultdict(list)
        for road in roads:
            start = road[0]
            end = road[1]
            weight = road[2]
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        return graph

    def dijkstra(self, n, graph):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重
        dist_to = [float('inf')] * n
        # base case，start 到 start 的最短距离就是 0
        dist_to[0] = 0

        # 优先级队列，权重较小的排在前面
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq:
            # 当前节点状态
            cur_node = heapq.heappop(pq)
            cur_node_id = cur_node[1]
            cur_dist_from_start = cur_node[0]

            # 将 cur_node 的相邻节点装入队
            for nei in graph[cur_node_id]:
                # 下一个节点状态
                next_node_id = nei[0]
                # 看看从 cur_node 达到 next_node 的距离是否会更短
                dist_to_next_node = cur_dist_from_start + nei[1]

                # 如果有更短的走法，更新备忘录，同时加入优先级队列
                if dist_to_next_node < dist_to[next_node_id]:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_node_id))

        # 这里我们需要返回最短路径数组，因为DP里面要用，所以不需要遇到终点就结束
        return dist_to

    def dp(self, node, n, graph, total_time, memo, mod, dist_to):
        # 走到终点了，计数
        if node == n - 1 and total_time == 0:
            return 1

        if memo[node][total_time] != -1:
            return memo[node][total_time]

        sub = 0
        for nei in graph[node]:
            next_node_id = nei[0]
            time = nei[1]
            if total_time - time < 0:
                continue
            # 主要优化在这里，只有到达下一个节点的最短路径等于当前节点最短路径 + 时间的时候才一定是最短路径，其它路径都可以不用继续遍历
            if dist_to[next_node_id] == dist_to[node] + time:
                sub += self.dp(next_node_id, n, graph, total_time - time, memo, mod, dist_to)
                sub %= mod

        memo[node][total_time] = sub

        return memo[node][total_time]

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Time O(e + e * log(e) + t * n)
        Space O(n * t)
        同理思路1，这里采用了一点优化的，但是备忘录会超memory，因为最短时间可能很大。详细见注释。
        """
        # 同思路1
        mod = 10 ** 9 + 7
        graph = self.build_graph(roads)
        dist_to = self.dijkstra(n, graph)
        # 同思路1，这里备忘录太大了，超memory
        memo = [[-1] * (int(dist_to[-1]) + 1) for _ in range(n)]

        res = self.dp(0, n, graph, dist_to[-1], memo, mod, dist_to)

        return res


class Solution3:
    def build_graph(self, roads):
        graph = defaultdict(list)
        for road in roads:
            start = road[0]
            end = road[1]
            weight = road[2]
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        return graph

    def dijkstra(self, n, graph):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重
        dist_to = [float('inf')] * n
        # base case，start 到 start 的最短距离就是 0
        dist_to[0] = 0

        # 优先级队列，权重较小的排在前面
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq:
            # 当前节点状态
            cur_node = heapq.heappop(pq)
            cur_node_id = cur_node[1]
            cur_dist_from_start = cur_node[0]

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

        return dist_to

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Time O(e + e * log(e) + t * n)
        Space O(n * t)
        同理思路2，但是这里对备忘录采用了一点优化，采用Python内置的缓存机制，保证了memory不会超。
        """
        # 同思路2
        mod = 10 ** 9 + 7
        graph = self.build_graph(roads)
        # 拿到最短路径备忘录数组
        dist_to = self.dijkstra(n, graph)

        # 写内置的function，保证输入的argument就是所有状态
        @cache
        def dp(node, total_time):
            # 整体DP思路和思路2一样，只是换成Python内置的缓存机制写
            if node == n - 1 and total_time == 0:
                return 1

            sub = 0
            for nei in graph[node]:
                next_node_id = nei[0]
                time = nei[1]
                if total_time - time < 0:
                    continue
                if dist_to[next_node_id] == dist_to[node] + time:
                    sub += dp(next_node_id, total_time - time)
                    sub %= mod

            return sub

        res = dp(0, dist_to[-1])

        return res


class Solution4:
    def build_graph(self, roads):
        graph = defaultdict(list)
        for road in roads:
            start = road[0]
            end = road[1]
            weight = road[2]
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        return graph

    def dijkstra(self, n, graph, mod):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重
        dist_to = [float('inf')] * n
        # 定义：ways[i] 的值就是起点 start 到达节点 i 的最短路径权重的路径个数
        ways = [0] * n
        # base case，start 到 start 的最短距离就是 0
        dist_to[0] = 0
        # base case，start 到 start 的最短距离个数就是 1
        ways[0] = 1

        # 优先级队列，权重较小的排在前面
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq:
            # 当前节点状态
            cur_node = heapq.heappop(pq)
            cur_node_id = cur_node[1]
            cur_dist_from_start = cur_node[0]

            # 将 cur_node 的相邻节点装入队
            for nei in graph[cur_node_id]:
                # 下一个节点状态
                next_node_id = nei[0]
                # 看看从 cur_node 达到 next_node 的距离是否会更短
                dist_to_next_node = cur_dist_from_start + nei[1]

                # 如果路径等于当前下一个节点最近的最短路径，说明我们找到了另一条到达下一个节点最短路径的走法
                if dist_to_next_node == dist_to[next_node_id]:
                    # 此时需要叠加路径个数
                    ways[next_node_id] += ways[cur_node_id]
                # 如果有更短的走法，更新两个备忘录，同时加入优先级队列
                elif dist_to_next_node < dist_to[next_node_id]:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_node_id))
                    # 此时说明有新的更短的路径，我们需要更新下一个节点对应的最短路径个数的备忘录
                    ways[next_node_id] = ways[cur_node_id]

        # 返回终点路径个数
        return ways[n-1] % mod

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        Time O(e + e * log(e))
        Space O(n)
        其实这题可以完全不需要再DP找合理的路径个数，可以直接在计算最短路径的时候同时找到最短路径下对应的路径个数，详细见注释。
        """
        mod = 10 ** 9 + 7
        graph = self.build_graph(roads)
        shortest_time_path_count = self.dijkstra(n, graph, mod)

        return shortest_time_path_count


s = Solution3()
print(s.countPaths(n=7, roads=[[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                               [0, 4, 5], [4, 6, 2]]))
