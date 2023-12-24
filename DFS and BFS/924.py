import collections
from typing import List


class Solution:
    def __init__(self):
        self.path = []

    def dfs(self, node, graph, visited):

        self.path.append(node)
        visited[node] = True
        for i in range(len(graph[node])):
            if graph[node][i] == 0:
                continue
            if visited[i]:
                continue
            self.dfs(i, graph, visited)

        return

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        """
        Time O(k * n^2)
        Space O(n)
        对于所有initial里面的节点我们遍历整个graph，记录每个节点走过的所有path，然后再遍历一次所有initial节点，统计出此节点外，
        其它initial节点包含的unique的path的节点个数，个数越少说明我们应该移除当前节点。此方法也可以过所有测试，但是我们需要遍历
        initial节点个数次的整个graph，对于在同一个component里面的节点没有必要重复遍历。
        """
        n = len(graph)
        node_to_path = {}
        min_node = float('inf')
        res = initial[0]
        # 遍历所有initial里面的节点，并记录每个节点的path
        for node in initial:
            visited = [False] * n
            self.path = []
            self.dfs(node, graph, visited)
            node_to_path[node] = self.path
        # 遍历initial里面除当前外的initial节点，统计可以覆盖到的unique节点个数
        for node in initial:
            tmp = []
            for other in initial:
                if other == node:
                    continue
                tmp += node_to_path[other]
            # 次个数就是会被infect到的节点个数，选取最小值，则为当前可以被移除的节点
            infect_node = len(set(tmp))
            if infect_node < min_node:
                res = node
                min_node = infect_node
            elif infect_node == min_node and node < res:
                res = node

        return res


class Solution2:
    def dfs(self, node, color, graph, colors):
        colors[node] = color
        for nei, adj in enumerate(graph[node]):
            if adj and nei not in colors:
                self.dfs(nei, color, graph, colors)

    def minMalwareSpread(self, graph, initial):
        """
        Time O(n^2)
        Space O(n)
        给每个node上颜色，同一个component里面的颜色是一样的。对于initial里面的node，如果两个node的颜色是一样的也就是在同一个component
        里面，此时remove任何一个node都没有用，因为最后都会spread到整个component。所以我们需要找的是在initial里面只有一个颜色的node，
        同时选出对比此node在的component包含node最多的节点，就是我们要移除的node。
        """
        # 1. Color each component.
        # colors[node] = the color of this node.
        n = len(graph)
        colors = {}
        c = 0

        for node in range(n):
            if node not in colors:
                self.dfs(node, c, graph, colors)
                c += 1

        # 2. Size of each color.
        # size[color] = number of occurrences of this color.
        # 此color下的component有多少个node
        size = collections.Counter(colors.values())

        # 3. Find unique colors in initial node.
        # 找到initial里面的node没有和其它initial节点存在于同一个component的node
        color_count = collections.Counter()
        for node in initial:
            color_count[colors[node]] += 1

        # 4. Answer
        ans = float('inf')
        for x in initial:
            c = colors[x]
            # 此节点的component只出现过一次在initial里面
            if color_count[c] == 1:
                # 第一次出现此节点
                if ans == float('inf'):
                    ans = x
                # 此节点对应的component的size更大
                elif size[c] > size[colors[ans]]:
                    ans = x
                # 此节点对应的component的size一样，但是index更小
                elif size[c] == size[colors[ans]] and x < ans:
                    ans = x
        # 还有一种情况就是所有在initial里面的节点都在同一个component里面，此时选取最小index的即可，因为remove任何一个效果都一样
        return ans if ans < float('inf') else min(initial)


s = Solution2()
print(s.minMalwareSpread(graph=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], initial=[1, 2]))
print(s.minMalwareSpread(graph=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], initial=[0, 2]))
print(s.minMalwareSpread(graph=[[1, 1, 0], [1, 1, 0], [0, 0, 1]], initial=[0, 1]))
print(s.minMalwareSpread(graph=[[1, 1, 0], [1, 1, 0], [0, 0, 1]], initial=[0, 1, 2]))
print(s.minMalwareSpread(graph=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], initial=[3, 1]))
