from typing import List, Any


class Solution:
    def __init__(self):
        self.largest_color_value = 0

    def build_graph(self, n: int, edges: List[List[int]]) -> tuple[list[list[Any]], list[int]]:
        # 建图函数
        # 图中共有 n 个节点
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for edge in edges:
            start, end = edge[0], edge[1]
            # 在图中添加一条从 start 指向 end 的有向边
            graph[start].append(end)
            in_degree[end] += 1

        return graph, in_degree

    def bfs(self, graph, in_degree, colors) -> int:
        # 根据入度初始化队列中的节点
        q = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        # 记录拓扑排序走到每个节点的时候，每个颜色对应的最大频率
        # 这里用26位数组记录，因为最多就26个字母
        topological_sort = [[0] * 26 for _ in range(len(in_degree))]
        count = 0
        # 开始执行 BFS 算法
        while q:
            cur = q.pop(0)
            # 累计走过节点的个数
            count += 1
            # 弹出节点的顺序即为拓扑排序结果
            # 当前节点颜色对应的index
            cur_color_index = ord(colors[cur]) - 97
            # 此时累加当前节点对应颜色的频率
            topological_sort[cur][cur_color_index] += 1
            # 最大值只可能在之前邻居节点走到的最大值，或者当前节点累加后产生新的最大值
            self.largest_color_value = max(self.largest_color_value, topological_sort[cur][cur_color_index])
            for nei in graph[cur]:
                # 更新邻居节点每个颜色对应的最大值频率，这里有可能多条路径走到邻居节点，所以需要取最大值
                for i in range(26):
                    topological_sort[nei][i] = max(topological_sort[nei][i], topological_sort[cur][i])

                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return count

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        Time O(26 * m + 26 * n) -> O(m + n)
        Space O(m + 26 * n) -> O(m + n)
        核心思想还是拓扑排序和动态规划的思路，如果有一条edge链接u -> v，走到v的时候color的frequency的情况应该是，走到u的时候情况加上v本身
        color的频率，也就是说最大值可能是在加完之后本身的color频率里面或者在之前出现过的走到u的color里面，所以如果是之前出现过的，那么走到
        u的时候已经计算出来了，如果是当前加完之后的频率，那么需要对比之前的最大值和当前加完之后的频率。详细见注释。
        """
        n = len(colors)
        # 构件图
        graph, in_degree = self.build_graph(n, edges)
        # 执行拓扑排序算法，计算走过的个数
        count = self.bfs(graph, in_degree, colors)

        return -1 if count != n else self.largest_color_value


s = Solution()
print(s.largestPathValue(colors="hhqhuqhqff",
                         edges=[[0, 1], [0, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7], [6, 7], [7, 8], [3, 8], [5, 8],
                                [8, 9], [3, 9], [6, 9]]))
