import heapq
from collections import defaultdict
from typing import List


class Solution:
    def build_graph(self, edges):

        graph = defaultdict(list)
        for edge in edges:
            start = edge[0]
            end = edge[1]
            graph[start].append(end)
            graph[end].append(start)

        return graph

    def dijkstra(self, n, graph, time, change):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重，注意这里是1开始的节点，并且需要两个数组维护最短top 2距离
        dist_to_1 = [float('inf')] * (n + 1)
        dist_to_2 = [float('inf')] * (n + 1)
        # 记录节点弹出的频率，因为最多两次
        freq = [0] * (n + 1)
        # base case，start 到 start 的最短距离就是 0
        dist_to_1[1] = 0

        # 优先级队列，权重较小的排在前面
        pq = []
        heapq.heappush(pq, (0, 1))

        while pq:
            # 当前节点状态
            # 此题有点trick的地方是，如果不是重点需要考虑红绿灯的等待情况，如果是重点则不需要，所以我们把当前节点的所有状态处理写在弹出后
            # 而不是在处理邻居节点的时候写，这样保证先check是否是第二次达到终点，再去考虑红绿灯的情况
            cur_dist_from_start, cur_node_id = heapq.heappop(pq)
            # 当前节点频率 +1
            freq[cur_node_id] += 1

            # 如果第二次到达终点，直接返回路径，不需要红绿灯的计算
            if freq[cur_node_id] == 2 and cur_node_id == n:
                return cur_dist_from_start

            # 如果当前节点遇到的是红灯
            if (cur_dist_from_start // change) % 2:
                # 当前时间 + 等待下一次绿灯的时间 + 实际走过edge的时间
                dist_to_next_node = cur_dist_from_start + (change - cur_dist_from_start % change) + time
            else:
                # 当前时间 + 实际走过edge的时间
                dist_to_next_node = cur_dist_from_start + time

            # 将 cur_node 的相邻节点装入队
            for nei in graph[cur_node_id]:
                # 下一个节点
                next_node_id = nei

                # 如果已经弹出了两次，则不能再走过了
                if freq[next_node_id] == 2:
                    continue

                # 如果小于最短路径，更新备忘录，同时加入优先级队列
                if dist_to_next_node < dist_to_1[next_node_id]:
                    dist_to_1[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_node_id))
                # 如果大于最短路径但是小于第二短路径，同时需要不等于第一短路径，这里有一种情况是有两条一模一样路径长度的path
                # 此时第二条一模一样的路径长度的path不能算作第二短的路径，更新备忘录，同时加入优先级队列
                elif dist_to_next_node < dist_to_2[next_node_id] and dist_to_1[next_node_id] != dist_to_next_node:
                    dist_to_2[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, (dist_to_next_node, next_node_id))

        return 0

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        """
        Time O(n + e * log(n))  dijkstra: e * log(e), e = n * (n - 1) --> e * log(n^2) --> e * log(n)
        Space O(n + e)
        还是利用最短路径的思路，这是这里我们需要计算的第二短的路径，也就是需要两个数组来记录起点到每个点的最短top 2路径。红绿灯的思路有点
        数学trick，当你在奇数倍数的红绿灯变化频率内的时候，一定是红灯，反之是绿灯。详细公式见注释。
        """
        graph = self.build_graph(edges)

        second_minimum_time = self.dijkstra(n, graph, time, change)

        return second_minimum_time


s = Solution()
print(s.secondMinimum(n=2, edges=[[1, 2]], time=3, change=2))
print(s.secondMinimum(n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5))
