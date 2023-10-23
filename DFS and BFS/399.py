from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.result = 0

    def dfs(self, graph, start, end, visited, cur_value):
        # visited集合加入当前节点
        visited.add(start)

        if start in graph:
            # 对节点的所有邻居节点开始遍历
            for nei in graph[start]:
                # 拿到下一个节点和权重
                next_start, value = nei[0], nei[1]
                # 如果节点不在图内，跳过
                if next_start not in graph:
                    continue
                # 如果访问过，跳过
                if next_start in visited:
                    continue

                # 记录当前节点到下一个点的乘积
                cur_value *= value
                # 如果是终点，直接赋值，结束递归
                if next_start == end:
                    self.result = cur_value
                    return
                # 如果不是重点，继续递归
                self.dfs(graph, next_start, end, visited, cur_value)
                # 这里一定要回溯撤销之前的乘积，当离开邻居节点的选择时候。
                # 回溯和递归是一对，如果在loop外计算乘积，则回溯也是在loop外，处理的是离开当前节点的逻辑
                # 如果在loop内，类似backtracking，处理的是离开邻居节点这条边的逻辑
                cur_value /= value
        else:
            return

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Time O(n_q * E)     each query loop whole graph edges
        Space O(V)          store all node in graph
        首先构建双向graph，每个节点是公式里面的变量，权重是相除的结果，ex: a / b = 1 则有 a: [(b, 1)]。
        遍历每个query，我们要找的就是一条合理的链接起点和终点的path在graph里面，并且相乘整个path上的所有权重，就是结果。
        我们可以用前序遍历的思路，每次处理当前节点逻辑，得到起点到当前节点的path的乘积，并通过递归传下去。如果遇到终点，全局变量记录最终结果。
        不采用后续遍历的思路是因为，如果用后续遍历并且带返回值的方式，需要在当前节点判断所有子节点也就是所有可能的path链接的返回结果。
        这样没必要，直接找到合理的path就结束递归。
        总结来说：
            1. 前序遍历 + 全局变量，用来在图内找一条合理的path并结束。
            2. 后续遍历 + 返回值，用来处理子结果，特别是如果子结果可以推父结果的题型，带上备忘录就 dp 的 DFS 写法。
        """
        graph = defaultdict(list)
        # 构建graph
        for i in range(len(equations)):
            first, second = equations[i][0], equations[i][1]
            # 双向图，反过来就是倒数
            graph[first].append((second, values[i]))
            graph[second].append((first, 1 / values[i]))

        # 遍历整个queries
        results = []
        for query in queries:
            start = query[0]
            end = query[1]
            # 如果分子分母一样
            if start == end:
                # 如果在图里面，则说明结果为 1
                if start in graph:
                    results.append(1)
                # 如果不在图里面，说明一定是 -1
                else:
                    results.append(-1)
            # 如果不一样，进入图找合理的path
            else:
                # 初始化visited集合，来记录不走回头路
                visited = set()
                # 初始化每次的全局变量，记录最终结果
                self.result = 0
                # 开始递归
                self.dfs(graph, start, end, visited, 1)
                # 如果结果没变，说明有不在图内的数，返回 -1
                results.append(-1 if self.result == 0 else self.result)

        return results


s = Solution()
print(s.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                     queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print(s.calcEquation(equations=[["x1", "x2"], ["x2", "x3"], ["x1", "x4"], ["x2", "x5"]], values=[3.0, 0.5, 3.4, 5.6],
                     queries=[["x2", "x4"], ["x1", "x5"], ["x1", "x3"], ["x5", "x5"], ["x5", "x1"], ["x3", "x4"],
                              ["x4", "x3"], ["x6", "x6"], ["x0", "x0"]]))
print(s.calcEquation(equations=[["x1", "x2"]], values=[3.0], queries=[["x9", "x2"], ["x9", "x9"]]))
