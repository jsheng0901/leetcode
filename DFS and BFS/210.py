from collections import defaultdict
from typing import List


class Solution:
    """
    Time O(v+e), v is number of vertex, e is number of edge,
    Space O(v+e)
    """

    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)
        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        order = []
        is_possible = True
        # white as no pass, gray as pass, black as finish to end node
        color = {k: 'white' for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return

            color[node] = 'gray'
            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == 'white':
                        dfs(neighbor)
                    elif color[neighbor] == 'gray':
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False
            # Recursion ends. We mark it as black
            # we store last finish course into stack first, like post order
            color[node] = 'black'
            order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == 'white':
                dfs(vertex)

        return order[::-1] if is_possible else []


class Solution2:
    def __init__(self):
        self.path = None
        self.visited = None
        self.result = []
        self.cycle = False

    def dfs(self, course_dict, course):
        # 发现环，直接结束
        if self.path[course]:
            self.cycle = True
            return
        # 发现环，或者已经访问过，等价于走到终点，直接结束
        if self.cycle or self.visited[course]:
            return

        # 前序遍历位置，记录当前节点访问过
        self.path[course] = True
        self.visited[course] = True

        for nei in course_dict[course]:
            self.dfs(course_dict, nei)

        # 后序遍历位置，记录离开当前节点，同时加入result结果数组
        self.path[course] = False
        self.result.append(course)

        return

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Time O(m + n) 初始化dict用O(m)，dfs走遍所有course用O(n)v
        Space O(m + n) 初始化dict用O(m)，dfs走遍所有course用O(n)，初始化visited和check用O(n)
        同207逻辑，一模一样。另外需要再后序遍历的位置加如进result结果的逻辑，因为是从后往前叠加，最终数组倒序一下就行。
        """
        course_dict = defaultdict(list)
        for p in prerequisites:
            next_course, prev_course = p[0], p[1]
            course_dict[prev_course].append(next_course)

        self.path = [False] * numCourses
        self.visited = [False] * numCourses

        for course in range(numCourses):
            self.dfs(course_dict, course)

        # 有环图无法进行拓扑排序
        if self.cycle:
            return []
        else:
            # 逆后序遍历结果即为拓扑排序结果
            return self.result[::-1]


class Solution3:
    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        # 建图函数
        # 图中共有 numCourses 个节点
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            from_course, to_course = edge[1], edge[0]
            # 修完课程 from 才能修课程 to
            # 在图中添加一条从 from 指向 to 的有向边
            graph[from_course].append(to_course)
        return graph

    def bfs(self, graph, in_degree, num_course):
        # 根据入度初始化队列中的节点，和环检测算法相同
        q = []
        for i in range(num_course):
            if in_degree[i] == 0:
                q.append(i)

        # 记录拓扑排序结果
        res = []
        # 记录遍历节点的顺序（索引）
        count = 0
        # 开始执行 BFS 算法
        while q:
            cur = q.pop(0)
            # 弹出节点的顺序即为拓扑排序结果
            res.append(cur)
            count += 1
            for next_course in graph[cur]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)

        if count != num_course:
            # 存在环，拓扑排序不存在
            return []

        return res

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Time O(m + n) 初始化dict用O(m)，bfs走遍所有course用O(n)
        Space O(m + n) 初始化dict用O(m)，bfs走遍所有course用O(n)
        同思路2，区别在于这里是用BFS的写法写拓扑排序。
        """
        # 建图，和环检测算法相同
        graph = self.buildGraph(numCourses, prerequisites)
        # 计算入度，和环检测算法相同
        in_degree = [0] * numCourses
        for edge in prerequisites:
            from_course, to_course = edge[1], edge[0]
            in_degree[to_course] += 1

        res = self.bfs(graph, in_degree, numCourses)

        return res


s = Solution3()
print(s.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
