from collections import defaultdict
from typing import List
import heapq


class Solution:
    def dfs(self, graph, node, dst, k, memo):
        # 如果遇到终点直接返回0，不需要价格
        if node == dst:
            return 0

        # 如果用完了所有边，则说明到不了，直接返回 -1
        if k == 0:
            return -1

        # 备忘录记录曾经到过的节点和边的情况，如果到过直接取值，不需要再遍历
        if memo[node][k] != -888:
            return memo[node][k]

        # 记录所有当前节点能到的目的地的返回值，此处也可以用一个参数记录，后面一直更新最小值即可
        res = []
        for nei in graph[node]:
            to = nei[0]
            price = nei[1]
            w = self.dfs(graph, to, dst, k - 1, memo)
            # 如果是 -1 说明到不了，不用进入结果计算，不然取 -1，最小值永远是 -1
            if w != -1:
                res.append(price + w)

        # 判断一下是否此节点的所有目的地都是不可行的，如果是则返回-1，不是说明有可行的path，返回最小值
        sub_price = -1 if len(res) == 0 else min(res)
        # 记录备忘录，离开当前节点时候
        memo[node][k] = sub_price

        return sub_price

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Time O(n)
        Space O(n)
        DFS思路也是dp的思路的DFS写法，核心思想，永远处理当前节点，loop里面处理下一个节点的判断或者返回的结果，loop结束处理离开当前节点，
        后续遍历的思路，在每次拿到返回值的时候，判断当前节点能到的所有目的地的最便宜的价格。
        然后自底向上返回最终结果。用备忘录记录到达节点并且还剩多少步的时候最便宜的价格。
        此题最特殊的是不需要visited数组来判断是否访问过，因为k会直接判断出是否还有足够的中转站能走，即使进入图中的环。
        另一个理由同 Dijkstra 中不需要带visited一样，如果带了visited数组，反而我们不一定会找到同一个node剩下k个path的情况下最短路径和，
        因为有时候节点可以重复访问。详细例子见测试数据倒数第二个。
        """
        # 先 +1 把中转站概念转化成多少条边
        k += 1
        # 初始化 graph
        graph = defaultdict(list)
        # 备忘录记录到达节点和剩多少边的时候最少价格，初始值无意义，随便设置，只要是没意义就行。
        memo = [[-888] * (k + 1) for _ in range(n)]
        # 构建图
        for flight in flights:
            dep = flight[0]
            arr = flight[1]
            price = flight[2]
            graph[dep].append([arr, price])

        total_price = self.dfs(graph, src, dst, k, memo)

        return total_price


class State:
    # 图节点的 id
    def __init__(self, id: int, cost_from_src: int, node_num_from_src: int):
        self.id = id
        self.cost_from_src = cost_from_src
        self.node_num_from_src = node_num_from_src

    def __lt__(self, other):
        return self.cost_from_src < other.cost_from_src


class Solution2:
    def dijkstra(self, start, end, graph, k):
        # 输入一个起点 src，计算从 src 到其他节点的最短距离

        # 定义：从起点 src 到达节点 i 的最短路径权重为 dist_to[i]
        dist_to = [float('inf') for _ in range(len(graph))]
        # 定义：从起点 src 到达节点 i 的最小权重路径至少要经过 node_num_to[i] 个节点
        node_num_to = [float('inf') for _ in range(len(graph))]

        # base case 初始化
        dist_to[start] = 0
        node_num_to[start] = 0

        # 优先级队列，cost_from_src 较小的排在前面
        pq = []
        # 从起点 src 开始进行 BFS
        heapq.heappush(pq, State(start, 0, 0))

        while pq:
            # 当前节点状态
            cur_state = heapq.heappop(pq)
            cur_node_id = cur_state.id
            cur_cost_from_src = cur_state.cost_from_src
            cur_node_num_from_src = cur_state.node_num_from_src

            if cur_node_id == end:
                # 找到最短路径，直接返回
                return cur_cost_from_src

            if cur_node_num_from_src == k:
                # 中转次数耗尽，跳到下一个节点
                continue

            # 将 cur_node 的相邻节点装入队列
            for neighbor in graph[cur_node_id]:
                # 下一个相邻节点状态
                next_node_id = neighbor[0]
                next_cost_from_src = cur_cost_from_src + neighbor[1]
                # 中转次数消耗 1
                next_node_num_from_src = cur_node_num_from_src + 1

                # 更新 dp table，备忘录，只有当找到最小权重和的时候才同时更新两个备忘录
                if next_cost_from_src < dist_to[next_node_id]:
                    dist_to[next_node_id] = next_cost_from_src
                    node_num_to[next_node_id] = next_node_num_from_src

                # 此处一定要有剪枝操作，不然特殊情况会超时，如果中转次数更多，花费还更大，那必然不会是最短路径
                if next_cost_from_src > dist_to[next_node_id] and next_node_num_from_src > node_num_to[next_node_id]:
                    continue
                # 次数是和传统模板不一样的地方，并不是一定只加入最小权重和path的节点，而是都加入。
                # 因为有k值限制，走到终点的路径次数并不一定都是一样的，最理想的情况可能受k限制。详细见测试数据最后一个例子。
                heapq.heappush(pq, State(next_node_id, next_cost_from_src, next_node_num_from_src))

        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Time O(E + Vlog(V)) E -> number of edges, V -> number of nodes。pq每个提取时间是log(v)，构建graph有E个边。
        Space O(E + V)  graph有E个边，备忘录有V个节点。
        Dijkstra 写法，不过此题和传统模板不一样的点在，第一需要多一个数组记录出发点到i点的中转次数，
        第二此题因为有k这个限制，我们并不能每次都只加入最短路径的节点进入优先级列队，而是所有情况下的都可以加入优先级列队，
        因为如果每次都是最短，会出现k先走完但是一开始并不是最短的路径没有加入优先级列队。详细例子见测试数据最后一个。
        """
        # 转化成边的条数
        k += 1
        # 构建图用list
        graph = [[] for _ in range(n)]

        for flight in flights:
            dep = flight[0]
            arr = flight[1]
            price = flight[2]
            graph[dep].append([arr, price])

        # 启动 dijkstra 算法
        # 计算以 src 为起点在 k 次中转到达 dst 的最短路径
        return self.dijkstra(src, dst, graph, k)


s = Solution2()
print(s.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                          src=0, dst=3, k=1))
print(s.findCheapestPrice(n=5, flights=[[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
                          src=2, dst=1, k=1))
print(s.findCheapestPrice(n=10, flights=[[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10], [6, 8, 6],
                                         [7, 9, 4], [1, 5, 4], [1, 0, 4], [9, 7, 3], [7, 0, 5], [6, 5, 8], [1, 7, 6],
                                         [4, 0, 9], [5, 9, 1], [8, 7, 3], [1, 2, 6], [4, 1, 5], [5, 2, 4], [1, 9, 1],
                                         [7, 8, 10], [0, 4, 2], [7, 2, 8]],
                          src=6, dst=0, k=7))
print(s.findCheapestPrice(n=5, flights=[[0, 1, 100], [0, 2, 100], [0, 3, 10], [1, 2, 100], [1, 4, 10], [2, 1, 10],
                                        [2, 3, 100], [2, 4, 100], [3, 2, 10], [3, 4, 100]],
                          src=0, dst=4, k=3))
print(s.findCheapestPrice(n=5, flights=[[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]],
                          src=0, dst=2, k=2))
