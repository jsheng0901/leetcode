from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.is_bipartion = True

    def dfs(self, graph, node, visited, color):
        # 如果已经确定不是二分图了，就不用浪费时间再递归遍历了
        if self.is_bipartion is False:
            return

        # 标记访问过节点，注意这里节点是从 1 开始的，而数组是0，也就是节点 i 代表数组的 i - 1
        visited[node - 1] = True
        for nei in graph[node]:
            # 相邻节点已经被访问过
            # 根据当前节点和相邻节点的颜色判断是否是二分图
            if visited[nei - 1]:
                # 若相同，则此图不是二分图，同时结束递归
                if color[nei - 1] == color[node - 1]:
                    self.is_bipartion = False
                    return
            # 相邻节点没有被访问过
            # 那么应该给节点邻居节点涂上和当前节点不同的颜色
            else:
                # 这里颜色用 true false 来标记
                color[nei - 1] = not color[node - 1]
                # 继续遍历邻居节点
                self.dfs(graph, nei, visited, color)

        return

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        Time O(n^2)
        Space O(n)
        二分图判定题，人看成节点，不喜欢代表链接的两个人及节点应该标记不同的颜色。不喜欢列表及图的列表。
        回归二分图模版，每次遍历节点，判断邻居节点是否访问过，没访问过则直接标记不一样的颜色，访问过就直接判断颜射是否一样，
        如果一样说明不可能是二分图，结束递归，返回全局变量记录是否是二分图。
        """
        # 初始化记录颜色，是否访问过和图
        color = [False] * n
        visited = [False] * n
        graph = defaultdict(list)

        # 建图
        for edge in dislikes:
            # 无向图，及双向图
            node1, node2 = edge[0], edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        # 因为图不一定是联通的，可能存在多个子图
        # 所以要把每个节点都作为起点进行一次遍历
        # 如果发现任何一个子图不是二分图，整幅图都不算二分图，同时结束loop循环
        # 从 1 开始，因为人是从 1 开始标记的
        for i in range(1, n + 1):
            # 如果已经不是二分图，则不可能直接break loop
            if self.is_bipartion is False:
                break
            # 如果没有访问过进入递归
            if visited[i - 1] is False:
                self.dfs(graph, i, visited, color)

        return self.is_bipartion


s = Solution()
print(s.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
