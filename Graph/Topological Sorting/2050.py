from collections import defaultdict
from typing import List


class Solution:

    def build_graph(self, n, relations):
        in_degree = [0] * (n + 1)
        graph = defaultdict(list)
        for relation in relations:
            start = relation[0]
            end = relation[1]
            graph[start].append(end)
            in_degree[end] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree, time):
        # 拓扑排序BFS模版
        queue = []
        # dp[i]表示走到i这堂课的最短时间
        dp = [0] * len(in_degree)
        # 记录最短总共所需时间
        total = 0
        # 所有入度为0的先加入，作为起点
        for i in range(1, len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
                # 记录所有起点所需的最短时间
                dp[i] = time[i - 1]
                # 更新总共最短时间
                total = max(total, dp[i])

        # 开始执行 BFS 算法
        while queue:
            cur = queue.pop(0)
            for nei in graph[cur]:
                # 更新走到当前邻居节点的时候，完成当前课程所需的最短时间，
                # 这里用的取最大值，是因为所有前置课程都必须要完成才能进进入后续课程，所以我们需要取所有前置课程的最大完成时间，可以同时学
                dp[nei] = max(dp[nei], time[nei - 1] + dp[cur])
                in_degree[nei] -= 1
                # 如果入度为0，说明在拓扑排序路上
                if in_degree[nei] == 0:
                    queue.append(nei)
                    # 入度为0的时候意味着当前课程已经完成了所有前置课程，可以进入当前课程和后面的课程，此时更新走到当前节点课程的最短总时间
                    total = max(dp[nei], total)

        return total

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        Time O(m + n)
        Space O(m + n)
        拓扑排序 + 动态规划的思路，完成所有课程的顺序是拓扑排序的结果，
        每一堂课程最短的完成时间 = 走到前置课程的最短完成时间 + 这堂课的时间。再更新完成所有课程所需要的最少时间。
        """
        # 构建图和入度数组
        graph, in_degree = self.build_graph(n, relations)

        # BFS拓扑排序，并且同时更新最短时间
        total = self.bfs(graph, in_degree, time)

        return total


s = Solution()
print(s.minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
print(s.minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
