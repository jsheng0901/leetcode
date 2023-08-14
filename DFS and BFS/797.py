from typing import List

# dfs 模板，和回溯几乎一模一样，因为回溯就是dfs的一种应用
# def dfs(图，参数):
#     if 终止条件:
#         存放结果
#         return
#
#     for 选择：本节点所连接的其他节点:
#         处理节点
#         dfs(图，选择的节点)    # 递归
#         回溯，撤销处理结果


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def dfs(self, graph, node):
        if node == len(graph) - 1:      # 当前节点index等于最后节点index时候说明找到终点，可以停止搜索
            # Python的list是mutable类型
            # 回溯中必须使用Deep Copy，来储存结果，否则之前存过的结果会随着回溯发生变化
            self.result.append(self.path[:])
            return

        for i in graph[node]:       # 本节点所连接的其他节点，遍历节点n链接的所有节点
            self.path.append(i)     # 遍历到的节点加入到路径中来
            self.dfs(graph, i)      # 进入下一层递归
            self.path.pop()         # 回溯，撤销本节点

        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Time O(v + e) v: node个数，e: edge个数，我们最多需要loop整个graph每个点每条边一次，当graph是adjacent list表示时候
        Space O(n) 存储结果的数组
        dfs经典应用，和回溯一模一样。
        """
        self.path.append(0)     # 初始化加入0节点
        self.dfs(graph, 0)      # 开始深搜
        return self.result
