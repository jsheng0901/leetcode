import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        Time O(n * log(m))
        Space O(n)
        用两个heap存储available的和unavailable的server。每次check是否有unavailable的server完成，
        如果完成了就先弹出来然后放进available的server，如果有free的server，就先处理free的server，之后计算当前task完成的时间，并存储进
        unavailable的server。详细见注释。
        """
        # 存储空闲的server
        free_servers = []
        for idx, weight in enumerate(servers):
            # 存储权重和index进free server
            heapq.heappush(free_servers, (weight, idx))

        # unavailable的server就是正在跑的task，存储task的完成时间，server的权重和，server对应的index
        unavailable_servers = []
        res = []

        for time, task in enumerate(tasks):
            # 如果有unavailable的完成了，先弹出来完成的server
            while unavailable_servers and unavailable_servers[0][0] <= time:
                _, weight, idx = heapq.heappop(unavailable_servers)
                # 并放进free的server
                heapq.heappush(free_servers, (weight, idx))

            # 如果有free的server
            if free_servers:
                # 弹出权重最小的，并且index在前面的
                weight, idx = heapq.heappop(free_servers)
                # 当前task用这个serve
                res.append(idx)
                # 当前task的完成时间
                finish_time = time + task
                # 房间unavailable的server
                heapq.heappush(unavailable_servers, (finish_time, weight, idx))
            # 如果没有free的server
            else:
                # 我们需要的是找下一个完成的server，unavailable的第一个server就是下一个最早完成的server，等这个server完成
                finish_time, weight, idx = heapq.heappop(unavailable_servers)
                # 当前task用这个serve
                res.append(idx)
                # 当前task的完成时间，是当前unavailable的完成时间 + task的处理时间，同时放进优先列队
                heapq.heappush(unavailable_servers, (finish_time + task, weight, idx))

        return res


s = Solution()
print(s.assignTasks(servers=[3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]))
print(s.assignTasks(servers=[5, 1, 4, 3, 2], tasks=[2, 1, 2, 4, 5, 2, 1]))
