from typing import List


class Solution:
    def __init__(self):
        # 记录图是否符合二分图性质
        self.is_bipartite = True

    def dfs(self, graph, node, color, visited):
        # 如果已经确定不是二分图了，就不用浪费时间再递归遍历了
        if self.is_bipartite is False:
            return

        # 标记访问过节点
        visited[node] = True
        for nei in graph[node]:
            # 相邻节点没有被访问过
            # 那么应该给节点邻居节点涂上和当前节点不同的颜色
            if visited[nei] is False:
                # 这里颜色用 true false 来标记
                color[nei] = not color[node]
                # 继续遍历邻居节点
                self.dfs(graph, nei, color, visited)
            else:
                # 相邻节点已经被访问过
                # 根据当前节点和相邻节点的颜色判断是否是二分图
                if color[nei] == color[node]:
                    # 若相同，则此图不是二分图，同时结束递归
                    self.is_bipartite = False
                    return

        return

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Time O(n^2)
        Space O(n)
        二分图模版题，每次遍历节点，判断邻居节点是否访问过，没访问过则直接标记不一样的颜色，访问过就直接判断颜射是否一样，
        如果一样说明不可能是二分图，结束递归，返回全局变量记录是否是二分图。
        """
        # 初始化记录颜色和是否访问过
        n = len(graph)
        color = [False] * n
        visited = [False] * n

        # 因为图不一定是联通的，可能存在多个子图
        # 所以要把每个节点都作为起点进行一次遍历
        # 如果发现任何一个子图不是二分图，整幅图都不算二分图，同时结束loop循环
        for i in range(n):
            if visited[i] is False:
                self.dfs(graph, i, color, visited)
                if self.is_bipartite is False:
                    break

        return self.is_bipartite


s = Solution()
print(s.isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
