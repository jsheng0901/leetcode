from collections import defaultdict
from typing import List


class Solution:
    def bfs(self, graph, in_degree):
        # 拓扑排序 BFS 模版
        #  根据入度初始化队列中的节点，起始点为叶子结点，无入度
        queue = []
        for i in range(1, len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        # 记录遍历节点的个数和图中的层数
        count = 0
        semester = 0
        # 开始执行 BFS 算法
        while queue:
            # 同一层节点，层数累加在此
            size = len(queue)
            semester += 1
            # 遍历同一层
            for _ in range(size):
                # 弹出节点的顺序即为拓扑排序结果
                front = queue.pop(0)
                # 记录遍历节点数量
                count += 1
                # 遍历邻居节点
                for nei in graph[front]:
                    # 入度 -1
                    in_degree[nei] -= 1
                    # 当入度没有的时候才进此节点
                    if in_degree[nei] == 0:
                        queue.append(nei)

        return count, semester

    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        Time O(n + e) n -> nodes  e -> edges
        Space O(n + e)
        拓扑排序标准模板题，BFS运用入度来实现拓扑排序的顺序。同207的逻辑。检查是否有环并且类似树的层序遍历，
        记录有多少层及多少semester去完成所有课程。
        """
        # 构建有向图和入度数组，记录每个点在图中的入度，注意这里入度的index要 +1 对应course
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for relation in relations:
            from_course, to_course = relation[0], relation[1]
            graph[from_course].append(to_course)
            in_degree[to_course] += 1

        # BFS计算走过的层数及semester和走过的节点个数
        count, semester = self.bfs(graph, in_degree)
        # 如果走过所有节点则无环，则直接返回层数，否则有环说明无法实现，返回 -1
        return semester if count == n else -1


class Solution2:
    def __init__(self):
        self.path = []
        self.cycle = False
        self.visited_length = {}

    def dfs(self, node, graph):
        # 如果之前访问过，并记录过最长路径，直接返回路径结果
        if node in self.visited_length:
            return self.visited_length[node]

        # 如果在单次路径中访问过此节点，说明有环
        if self.path[node]:
            # 全局遍历设置
            self.cycle = True
            # 有环直接返回 -1
            return -1

        # 如果有环直接返回 -1
        if self.cycle:
            return -1

        # 当前节点记录
        self.path[node] = True
        # 当前节点路径最大值
        max_length = 1
        for nei in graph[node]:
            # 子节点返回的访问路径最大值
            sub_length = self.dfs(nei, graph)
            # 如果是 -1 说明之前有环，最大长度为 -1
            if sub_length == -1:
                max_length = -1
            # 如果不是 -1，继续更新最大长度
            else:
                # 当前节点 + 子节点返回长度 或者之前的最大长度
                max_length = max(sub_length + 1, max_length)

        # 记录备忘录，当前节点对应的最大长度
        self.visited_length[node] = max_length
        # 回溯，离开当前节点的时候记得撤销访问过，因为还有可能从别的路径访问此节点
        self.path[node] = False
        # 返回最长长度
        return max_length

    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        Time O(n + e) n -> nodes  e -> edges
        Space O(n + e)
        DFS的写法，速度上理论上和BFS一样，不过因为这里的DFS有采用备忘录的写法，实际情况应该更快。DFS需要备忘录，所以必须使用后续遍历的方式。
        用返回值来判断是否需要继续遍历。同时和传统的判断拓扑排序是否有环不一样的地方在于，一般需要visited数组来记录访问节点，并且不需要重复
        访问节点，但是这里因为需要判断最长的长度，同一个节点可能有多个方式的path到达，所以这里并不需要visited数组来记录是否重复访问。相反
        需要访问所有路径，也就是即使重复的节点也需要不同的路径走一遍。详细进注释
        """
        # 构建graph
        graph = defaultdict(list)
        for relation in relations:
            from_course, to_course = relation[0], relation[1]
            graph[from_course].append(to_course)

        # 记录单次路径访问的节点，防止有环
        self.path = [False] * (n + 1)
        # 记录最终的学期
        semester = 1
        # 遍历所有节点
        for i in range(1, n + 1):
            # 如果有环直接返回 -1，不需要继续遍历
            if self.cycle:
                return -1
            # 得到当前节点作为起点的最长路径
            max_length = self.dfs(i, graph)
            # 记录全局最长路径也就是学期
            semester = max(max_length, semester)

        return semester


s = Solution2()
print(s.minimumSemesters(n=3, relations=[[1, 3], [2, 3]]))
s = Solution2()
print(s.minimumSemesters(n=3, relations=[[1, 2], [2, 3], [3, 1]]))
