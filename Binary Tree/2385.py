from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def traversal(self, node, pre_node, graph):
        # 前序遍历标准写法把树转化成图
        if node is None:
            return

        if pre_node:
            graph[node.val].append(pre_node.val)
            graph[pre_node.val].append(node.val)

        self.traversal(node.left, node, graph)
        self.traversal(node.right, node, graph)

        return

    def bfs(self, start, graph):
        # 标准BFS写法
        queue = [start]
        # 注意这里用set不能直接初始化set(1)
        visited = set()
        visited.add(start)
        # 注意这里初始值为-1，因为起始点就是1
        time = -1

        while queue:
            size = len(queue)
            time += 1
            for _ in range(size):
                top = queue.pop(0)
                for nei in graph[top]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

        return time

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Time O(n)
        Space O(n)
        先把树转化成图的结构，然后BFS遍历图找到起点到所有点的最短距离。
        """
        # 初始化双向图
        graph = defaultdict(list)
        # 前序遍历构建图
        self.traversal(root, None, graph)
        # BFS找最短距离到所有点
        time = self.bfs(start, graph)

        return time


class Solution2:
    def __init__(self):
        self.max_distance = 0

    def traverse(self, root, start):
        # 当前深度初始化
        depth = 0
        # 空节点返回0
        if root is None:
            return depth
        # 左子树深度
        left_depth = self.traverse(root.left, start)
        # 右子树深度
        right_depth = self.traverse(root.right, start)

        # 情况一，当前点是起始点，我们找到当前点最为subtree的根节点的最大深度，并记录
        if root.val == start:
            self.max_distance = max(left_depth, right_depth)
            # 这里返回-1是为了让当前节点的父节点知道子树里面包含了起点，这样计算深度的时候要改变方式
            depth = -1
        # 情况2，当前节点的子节点都不包含起点
        elif left_depth >= 0 and right_depth >= 0:
            # 则正常计算最大深度
            depth = max(left_depth, right_depth) + 1
        # 情况3，当前节点的子节点包含起点
        else:
            # 此时距离为当前另一半不包含起点的最大深度 + 当前节点到起点的深度，这里用绝对值因为我们遇到起点后返回的是负数表示距离
            distance = abs(left_depth) + abs(right_depth)
            # 同时更新起点到所有点的最大深度
            self.max_distance = max(self.max_distance, distance)
            # 这里的返回值很trick，当我们子节点包含起点后我们需要的返回值是当前节点到起点的距离而不再是返回最大深度
            # 所以这里我们找到最小值也就是包含子节点为起点的那个branch的depth，一定是负数这里，所以这里-1代表距离增加1
            depth = min(left_depth, right_depth) - 1

        return depth

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Time O(n)
        Space O(n)
        思路一其实要遍历两次树，但是我们可以只遍历一次树。核心思想是，当前点到所有点的最大距离应该来源于两个方向，一个是当前点作为subtree的
        根节点的时候的最大深度，另一个是当前点到实际根节点的距离，加上实际根节点不包含起始点的那个branch的最大深度。详细见注释。
        """
        self.traverse(root, start)

        return self.max_distance


node1 = TreeNode(1)
node2 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(6)
node6 = TreeNode(10)
node7 = TreeNode(9)
node8 = TreeNode(2)
node1.left = node2
node1.right = node3
node3.left = node6
node3.right = node5
node2.right = node4
node4.left = node7
node4.right = node8
s = Solution()
print(s.amountOfTime(node1, 3))
