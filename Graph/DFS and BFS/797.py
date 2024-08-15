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


class Solution1:
    def __init__(self):
        self.result = []
        self.path = []

    def dfs(self, graph, node):
        if node == len(graph) - 1:  # 当前节点index等于最后节点index时候说明找到终点，可以停止搜索
            # Python的list是mutable类型
            # 回溯中必须使用Deep Copy，来储存结果，否则之前存过的结果会随着回溯发生变化
            self.result.append(self.path[:])
            return

        for i in graph[node]:  # 本节点所连接的其他节点，遍历节点n链接的所有节点
            self.path.append(i)  # 遍历到的节点加入到路径中来
            self.dfs(graph, i)  # 进入下一层递归
            self.path.pop()  # 回溯，撤销本节点

        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Time O(v + e) v: node个数，e: edge个数，我们最多需要loop整个graph每个点每条边一次，当graph是adjacent list表示时候
        Space O(n) 存储结果的数组
        dfs经典应用，和回溯一模一样。
        """
        self.path.append(0)  # 初始化加入0节点
        self.dfs(graph, 0)  # 开始深搜
        return self.result


# 不同算法模板对比
# DFS 算法，关注点在节点
# def traverse(root: TreeNode):
#     if root is None:
#         return
#     print("进入节点", root)
#     for child in root.children:
#         traverse(child)
#     print("离开节点", root)
#
# 回溯算法，关注点在树枝
# def backtrack(root: TreeNode):
#     if root is None:
#         return
#     for child in root.children:
#         # 做选择
#         print("从", root, "到", child)
#         backtrack(child)
#         # 撤销选择
#         print("从", child, "到", root)

class Solution2:
    def __init__(self):
        self.result = []
        self.path = []

    def dfs(self, graph, node):
        # 添加节点 node 到路径
        self.path.append(node)

        # 到达终点
        if node == len(graph) - 1:
            # 记录此条路径
            self.result.append(self.path[:])
            # 需要注意是在这里要回溯一下，因为终点节点不会进入到loop后面的逻辑，及不会在后面pop out，所有要在这里弹出
            self.path.pop()
            return

        # 递归每个相邻节点
        for nei in graph[node]:
            self.dfs(graph, nei)

        # 从路径移出当前节点 s，走到loop外说明当前节点的所有邻居节点都处理完了，需要回到当前节点的上一个节点，及pop out当前节点。
        self.path.pop()

        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Time O(v + e)
        Space O(n)
        dfs模板题，此模板方法和回溯不一样的是，dfs先处理当前节点再进入邻居节点，最终在loop外处理当前节点的回溯及pop out。
        然而回溯模板是处理邻居节点在loop内，所以root节点及其实点需要在一开始就加入进path。
        换言之：
        如果加入path的处理在loop外，则pop out也应该在loop外，此时处理的是当前节点逻辑。
        如果加入path的处理在loop内，则pop out也应该在loop内，此时处理的是当前节点邻居节点的逻辑。
        也就是append和pop必须同时发现并且在同一层逻辑内。
        """
        self.dfs(graph, 0)

        return self.result


s = Solution2()
print(s.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
