import heapq
from typing import List


class State:
    def __init__(self, id_, prob_from_start):
        self.id = id_
        self.prob_from_start = prob_from_start

    def __lt__(self, other):
        """
       比大小用，当object进入比大小的method的时候，比如sort或者heapq，此method会被自动叫，用来比较是否obj1 > obj2在我们定义下
       """
        return self.prob_from_start > other.prob_from_start


class Solution:
    def dijkstra(self, start, end, graph):

        # 记录最短路径的权重，你可以理解为 dp table
        # 定义：prob_to[i] 的值就是节点 start 到达节点 i 的最大概率
        prob_to = [-1] * len(graph)
        # dp table 初始化为一个取不到的最小值
        # base case，start 到 start 的概率就是 1
        prob_to[start] = 1

        # 优先级队列，prob_from_start 较大的排在前面
        pq = []
        # 从起点 start 开始进行 BFS
        heapq.heappush(pq, State(start, 1))

        while pq:
            # 当前节点状态
            cur_state = heapq.heappop(pq)
            cur_node_id = cur_state.id
            cur_prob_from_start = cur_state.prob_from_start

            # 遇到终点提前返回
            if cur_node_id == end:
                return cur_prob_from_start

            if cur_prob_from_start < prob_to[cur_node_id]:
                # 已经有一条概率更大的路径到达 curNode 节点了，这里要反过来比较和求最小权重和不一样
                continue

            # 将 cur_node_id 的相邻节点装入队列
            for neighbor in graph[cur_node_id]:
                next_node_id = neighbor[0]
                prob_to_next_node = prob_to[cur_node_id] * neighbor[1]
                # 看看从 cur_node_id 达到 next_node_id 的概率是否会更大
                if prob_to[next_node_id] < prob_to_next_node:
                    prob_to[next_node_id] = prob_to_next_node
                    heapq.heappush(pq, State(next_node_id, prob_to_next_node))

        return 0

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        """
        Time O(E + Vlog(V)) E -> number of edges, V -> number of nodes。pq每个提取时间是log(v)，构建graph有E个边。
        Space O(E + V)  graph有E个边，备忘录有V个节点。
        本质上是 Dijkstra 模板题，Dijkstra 本质是算最优解，最大最小都可以。
        区别于记录最短路径的权重和，这里存储的是最大概率乘积，每次优先级列队拿出来的是最大的乘积概率路径，放进去的时候比较也是取最大值。
        """
        # 构建双向图，也就是无向图
        graph = [[] for _ in range(n)]
        # 加入每条边进图，每条边要加两次，因为是无向图
        for i in range(len(edges)):
            source = edges[i][0]
            target = edges[i][1]
            weight = succProb[i]
            graph[source].append([target, weight])
            graph[target].append([source, weight])

        return self.dijkstra(start_node, end_node, graph)


s = Solution()
print(s.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start_node=0, end_node=2))
