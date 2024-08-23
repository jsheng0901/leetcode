from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.diameter = 0

    def build_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        return graph

    def dfs(self, node, graph, count, visited):

        # 统计走到当前节点path的个数
        count += 1
        # 标记访问过
        visited[node] = True
        # 更新最长距离
        self.diameter = max(self.diameter, count - 1)

        # 遍历所有邻居节点
        for nei in graph[node]:
            # 访问过跳过
            if visited[nei]:
                continue
            self.dfs(nei, graph, count, visited)

        # 注意这里要回溯一下，因为同一个点可以不同路径多次访问
        visited[node] = False

        return

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Time O(n^2)
        Space O(n)
        每个点都找到能走到最远的距离，统计全局最远距离就是图的直径。但是这个方式特别费时，明显TLE。每个点会被多次遍历到。
        """
        # 构建图
        n = len(edges) + 1
        graph = self.build_graph(edges)

        # 每个点遍历一次全部的图
        for i in range(n):
            visited = [False] * n
            self.dfs(i, graph, 0, visited)

        return self.diameter


class Solution2:
    def __init__(self):
        self.diameter = 0
        self.furthest_node = None
        self.max_count = 0

    def build_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        return graph

    def dfs(self, node, graph, count, visited):

        # 当前节点个数
        count += 1
        # 标记访问过
        visited[node] = True
        # 更新此时的直径，这里直径等于节点个数 - 1
        self.diameter = max(self.diameter, count - 1)
        # 如果当前走到的距离更远
        if count > self.max_count:
            # 更新最远距离，并且更新最远节点
            self.max_count = count
            self.furthest_node = node

        # 继续遍历邻居节点
        for nei in graph[node]:
            if visited[nei]:
                continue
            self.dfs(nei, graph, count, visited)

        visited[node] = False

        return

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Time O(2n) --> O(n)
        Space O(n)
        对于一个图的直径，我们可以先从任意一个点走到最远的距离，之后这个最远的距离能走到的最远的距离，就是这个图的直径。
        先随机选一个点，找到能走到的最远距离遍历一次图，再把这个最远的距离点作为起点，找到最远的距离，此时的距离就是直径。
        """
        # 构建图
        n = len(edges) + 1
        graph = self.build_graph(edges)

        # 选取节点0作为起点，找到能走到的最远距离
        visited = [False] * n
        self.dfs(0, graph, 0, visited)

        # 最远距离作为起点，找到另一个能走到的最远距离，此时的距离就是直径
        visited = [False] * n
        self.dfs(self.furthest_node, graph, 0, visited)

        return self.diameter


class Solution3:
    def __init__(self):
        self.diameter = 0

    def build_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        return graph

    def dfs(self, node, graph, parent):
        # 当前节点所有子节点返回值里面对应的最长的两个值
        top_1_distance, top_2_distance = 0, 0
        # 遍历邻居节点
        for nei in graph[node]:
            # 这里直接把父节点传过来，方便判断是否走回头路，不需要visited数组
            if nei == parent:
                continue

            # 当前节点拿到的子节点返回值
            distance = self.dfs(nei, graph, node) + 1

            # 后续遍历位置，用两个指针来接住最长的两个距离
            # 如果大于最长的距离，则更新两个距离
            if distance > top_1_distance:
                # 注意这里一定要先更新第二个距离，再更新第一个，否则顺序颠倒的话第二个距离会等于第一个距离
                top_2_distance = top_1_distance
                top_1_distance = distance
                # 或者采用这种swap的形式写，同一行更新
                # top_1_distance, top_2_distance = distance, top_1_distance
            # 如果大于第二个，则只更新第二个距离
            elif distance > top_2_distance:
                top_2_distance = distance

        # 更新直径
        self.diameter = max(self.diameter, top_1_distance + top_2_distance)

        # 返回最长的距离
        return top_1_distance

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        Time O(n)
        Space O(n)
        其实此题和N叉树找直径是一模一样的思路，任何一个点都可以视作一个N叉树的根节点，我们需要找到的就是这个节点的子节点里面最长的两个距离，
        对于这个节点，此时的直径等于最长的两个距离之和 + 自己。之后我们返回最长的那个距离给父节点，利用后续遍历的思路层层递归上去，
        只需要遍历一次整个图。
        """
        graph = self.build_graph(edges)
        # 选取0作为整个图里面的根节点，任意一个节点都行，只是选择0比较方便
        self.dfs(0, graph, 0)

        return self.diameter


# s1 = Solution2()
# print(s1.treeDiameter(edges=[[0, 1], [0, 2]]))
s2 = Solution3()
print(s2.treeDiameter(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
