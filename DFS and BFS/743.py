from collections import defaultdict
from typing import Union


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


s = Solution()
print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
