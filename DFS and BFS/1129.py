from collections import defaultdict
from typing import List


class Solution:
    def bfs(self, red_graph, blue_graph, n):
        # 初始化结果数组 -1，如果走不到直接为 -1
        ans = [-1] * n
        # 初始化栈内0节点的状态，这里颜色标记为 None，表示可以去到任意节点
        queue = [(0, 0, None)]
        # 初始化两种颜色graph的访问集合，避免走回头路
        red_visited = set()
        blue_visited = set()
        red_visited.add(0)
        blue_visited.add(0)

        while queue:
            # 当前节点的状态，弹出时候即为离开节点的时候，处理当前节点，类似DFS前序遍历里面先处理当前节点
            node, length, edge_color = queue.pop(0)
            # 如果当前节点为 -1，说明走到新的节点，直接赋值给结果数组
            if ans[node] == -1:
                ans[node] = length
            # 如果不是 -1，说明之前走到过，取最小值
            else:
                ans[node] = min(ans[node], length)

            # 如果之前到达此节点的边是初始值或者红色edge，那我们遍历蓝色边构成的邻居节点
            if edge_color is None or edge_color == 'red':
                # 遍历邻居是蓝色edge的点
                for nei in blue_graph[node]:
                    # 如果没有访问过，则继续遍历
                    if nei not in blue_visited:
                        # 邻居节点如栈，长度 +1
                        queue.append((nei, length + 1, 'blue'))
                        # 记录访问过的节点
                        blue_visited.add(nei)

            # 同理上面红色edge
            if edge_color is None or edge_color == 'blue':
                for nei in red_graph[node]:
                    if nei not in red_visited:
                        queue.append((nei, length + 1, 'red'))
                        red_visited.add(nei)
        # 返回结果
        return ans

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        Time O(red_edge + blue_edge)
        Space O(n)
        BFS找最短路径，这里区别于传统BFS的是，我们有两个颜色的graph，但是我们可以有自循环或者双向循环的edge，
        那如何避免走死循环的方式在于构建两种颜色的graph，和visited集合，每一种颜色的点在visited里面只能访问一次，这样避免了死循环。
        其它要点就是正常的BFS找最短路径，我们入栈每次点的三种状态(节点id, 走到此时的长度, 走到此节点时候edge的颜色)
        """
        # 构建两种颜色的graph
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        for edge in redEdges:
            node1, node2 = edge[0], edge[1]
            red_graph[node1].append(node2)

        for edge in blueEdges:
            node1, node2 = edge[0], edge[1]
            blue_graph[node1].append(node2)
        # BFS找最短路径，从0节点开始，同时存储进结果
        ans = self.bfs(red_graph, blue_graph, n)

        return ans


s = Solution()
print(s.shortestAlternatingPaths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]))
print(s.shortestAlternatingPaths(n=3, redEdges=[[0, 1]], blueEdges=[[2, 1]]))
print(s.shortestAlternatingPaths(n=5, redEdges=[[0, 1], [1, 2], [2, 3], [3, 4]], blueEdges=[[1, 2], [2, 3], [3, 1]]))
print(s.shortestAlternatingPaths(n=3, redEdges=[[0, 1], [0, 2]], blueEdges=[[1, 0]]))
print(s.shortestAlternatingPaths(n=5, redEdges=[[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [2, 1], [2, 0], [1, 4], [3, 4]],
                                 blueEdges=[[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]))
