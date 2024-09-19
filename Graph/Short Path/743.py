from collections import defaultdict
from typing import Union
import heapq


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def bfs(self, signal_receive_at, k):
        # 加入初始node index
        queue = [k]
        # 初始化node时间到达时间开销为0
        signal_receive_at[k] = 0
        # 遍历整个graph
        while queue:
            curr_node = queue.pop(0)
            # 遍历当前出发node的所有邻居node
            for nei in self.graph[curr_node]:
                target, time = nei[0], nei[1]
                # 到达当前node的时间加上当前node到达邻居的时间则为，邻居node到达最开始初始node的最短总时间
                arrive_time = signal_receive_at[curr_node] + time
                # 判断是否是最小值
                if arrive_time < signal_receive_at[target]:
                    # 更新最小值
                    signal_receive_at[target] = arrive_time
                    queue.append(target)

    def networkDelayTime(self, times: [[int]], n: int, k: int) -> Union[int, float]:
        """
        N is number of total node, E is number of total edges,
        Time O(N * E) Each of the NNN nodes can be added to the queue for all the edges connected to it.
        Space O(N * E) graph will take O(E) space and the queue for BFS will use O(N⋅E)

        BFS写法，先把times转化成一个dictionary的graph，key代表出发点，value代表可以去到的目的地加时间开销
        用数组signal_receive_at记录每个node到初始node的最短时间开销，最终去数组里面的最大值表示到达所有node的总时间，
        如果存在无穷大说明有node无法从出发node到达，则直接返回-1
        """
        # 构建graph
        for t in times:
            source = t[0]
            target = t[1]
            time = t[2]
            self.graph[source].append((target, time))

        # 构建记录node到初始node最小距离的数组，初始化为inf，此处+1是因为node是1base index的
        signal_receive_at = [float('inf')] * (n + 1)
        # bfs遍历整个graph，从初始node开始并update signal_receive_at数组
        self.bfs(signal_receive_at, k)
        # 取signal_receive_at数组最大值代表可以去到所有点的最小时间
        answer = max(signal_receive_at[1:])
        # 判断是否有node无法到达
        if answer == float('inf'):
            return -1
        else:
            return answer


class State:
    # 图节点的 id
    def __init__(self, id_: int, dist_from_start: int):
        self.id = id_
        # 从 start 节点到当前节点的距离
        self.dist_from_start = dist_from_start

    def __lt__(self, other):
        """
        比大小用，当object进入比大小的method的时候，比如sort或者heapq，此method会被自动叫，用来比较是否obj1 < obj2在我们定义下
        """
        return self.dist_from_start < other.dist_from_start


class Solution2:
    def dijkstra(self, start, graph):
        """
        Dijkstra 算法模版，输入一个起点 start，计算从 start 到其他节点的最短距离
        """
        # 定义：dist_to[i] 的值就是起点 start 到达节点 i 的最短路径权重
        dist_to = [float('inf')] * len(graph)
        # base case，start 到 start 的最短距离就是 0
        dist_to[start] = 0

        # 优先级队列，dist_from_start 较小的排在前面
        pq = [State(start, 0)]
        # 从起点 start 开始进行 BFS
        heapq.heapify(pq)

        while pq:

            # 当前节点状态
            cur_state = heapq.heappop(pq)
            cur_node_id = cur_state.id
            cur_dist_from_start = cur_state.dist_from_start

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

                # 如果有更短的走法，更新备忘录，同时加入优先级队列
                if dist_to_next_node < dist_to[next_node_id]:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(pq, State(next_node_id, dist_to_next_node))

        return dist_to

    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        """
        Time O(n + e * log(n)) e是边的个数，n是节点个数
        Space O(n)
        本质上是 Dijkstra 模板题，而 Dijkstra 本质上贪心原则下带备忘录的BFS算法。
        不需要visited数组记录，因为算法里面每次都是储存最短的路径，两个点之间一定会有最短路径不会一直循环下去。
        而且加权图中的 Dijkstra 算法和无权图中的普通 BFS 算法不同，在 Dijkstra 算法中，你第一次经过某个节点时的路径权重，
        不见得就是最小的，所以对于同一个节点，我们可能会经过多次，而且每次的 dist_from_start 可能都不一样。所以不用visited数组记录path。
        """

        # 节点编号是从 1 开始的，所以要一个大小为 n + 1 的邻接表
        graph = [[] for _ in range(n + 1)]
        for edge in times:
            source = edge[0]
            target = edge[1]
            time = edge[2]
            # source -> List<(target, time)>
            # 邻接表存储图结构，同时存储权重信息
            graph[source].append([target, time])

        # 启动 dijkstra 算法计算以节点 k 为起点到其他节点的最短路径
        dist_to = self.dijkstra(k, graph)

        # 找到最长的那一条最短路径
        res = 0
        for i in range(1, len(dist_to)):
            if dist_to[i] == float('inf'):
                # 有节点不可达，返回 -1
                return -1
            res = max(res, dist_to[i])
        return res


s = Solution2()
print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
