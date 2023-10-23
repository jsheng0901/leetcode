from typing import List


class Solution:
    def dfs(self, graph, node, visited):
        # DFS处理前序遍历逻辑，永远处理当前节点
        visited[node] = True
        # 遍历所有邻居节点
        for i in range(len(graph[node])):
            # 访问过，跳过
            if visited[i]:
                continue
            # 没有链接起来，跳过
            if graph[node][i] == 0:
                continue
            # 合理的链接的节点，进入递归
            self.dfs(graph, i, visited)

        return

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n)
        DFS 模板题，走一遍所有的点，每次DFS走完所有链接起来的点并标记起来，总共有多少条不连接的path，就是多少个省。
        """
        # visited数组记录是否访问过，不走重复的点
        n = len(isConnected)
        visited = [False] * n
        num_province = 0

        # 遍历所有节点
        for i in range(n):
            # 如果没有访问过说明是一个新的path开始，进入递归
            if visited[i] is False:
                num_province += 1
                self.dfs(isConnected, i, visited)

        return num_province


s = Solution()
print(s.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum(isConnected=[[1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0],
                                   [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1]]))
