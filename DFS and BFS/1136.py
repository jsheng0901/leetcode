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


s = Solution()
print(s.minimumSemesters(n=3, relations=[[1, 3], [2, 3]]))
