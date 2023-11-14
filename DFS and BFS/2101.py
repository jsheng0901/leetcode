from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.num_detonate = 0

    def get_dist(self, x, y):
        dist = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1 / 2)

        return dist

    def dfs(self, node, graph, visited):
        # 处理当前节点，前序遍历思路，进DFS的一定是valid过的节点，不需要递归判断结束
        # 全局变量记录到达点的个数
        self.num_detonate += 1
        # 记录访问过，防止走回头路
        visited[node] = True
        # 继续递归邻居节点
        for nei in graph[node]:
            # 判断下一个节点
            if visited[nei] is False:
                # 继续递归
                self.dfs(nei, graph, visited)

        return

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """
        Time O(n^3)
        Space O(n^2)
        转化问题为graph，先构建graph，如果点i可以到达点j则，i -> j。此步骤需要n^2时间和n^2空间最差情况下。每个点之间都可以相互抵达，
        注意此graph并不是无向图，相反是有向图，因为每个点的半径r并不一样。之后就是DFS遍历整个graph，可以走到点最多的个数就是最终能引爆
        炸弹最多的个数。DFS这里遍历注意我们需要每次都初始化visited数组，因为某个点作为起始点访问过并不代表其它点作为起始点访问时不能走到。
        例如测试数据的第二个例子。因为每个点我们都需要遍历一次整个图，所以最差情况n * edges(n^2) -> n^3的时间。
        此题基本上是DBSCAN算法的雏形部分。
        """
        graph = defaultdict(list)
        # 构建有向图，计算是否在半径内，注意这里要遍历所有两两pair
        for i in range(len(bombs)):
            x = bombs[i][:2]
            r = bombs[i][2]
            for j in range(len(bombs)):
                # 如果不是同一个点继续计算
                if i != j:
                    y = bombs[j][:2]
                    dist = self.get_dist(x, y)
                    # 在半径内，构建edge进graph
                    if dist <= r:
                        graph[i].append(j)

        # 计算最大可到达的点的个数
        max_detonate = float('-inf')
        # 遍历所有图中点
        for i in range(len(bombs)):
            # 初始化visited数组
            visited = [False] * len(bombs)
            # 初始化每次可以到达点的个数
            self.num_detonate = 0
            # 开始DFS递归
            self.dfs(i, graph, visited)
            # 更新最大可到达点的个数
            max_detonate = max(max_detonate, self.num_detonate)

        return max_detonate


s = Solution()
print(s.maximumDetonation(bombs=[[2, 1, 3], [6, 1, 4]]))
print(s.maximumDetonation(bombs=[[1, 1, 5], [10, 10, 5]]))
print(s.maximumDetonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
