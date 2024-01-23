from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def traversal(self, node, par=None):
        if node is None:
            return
        # 添加parent节点给每个node
        node.par = par
        self.traversal(node.left, node)
        self.traversal(node.right, node)

        return

    def bfs(self, target, k):
        queue = [(target, 0)]
        visited = {target}

        while queue:
            # 如果当前节点等于k，说明此时queue里面都是同一个step的节点，直接全部添加并返回
            if queue[0][1] == k:
                return [node.val for node, step in queue]

            # 遍历所有邻居
            node, step = queue.pop(0)
            for nei in (node.left, node.right, node.par):
                if nei and nei not in visited:
                    queue.append((nei, step + 1))
                    visited.add(nei)

        return []

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> [int]:
        """
        Time O(n)
        Space O(n)
        先做前序遍历给所有节点赋值parent属性，然后遍历新的tree，bsf查找距离，bfs存储当前节点的状态，包括节点value和节点step。
        """
        self.traversal(root)

        return self.bfs(target, k)


class Solution2:
    def build_graph(self, graph, cur, parent):
        if cur and parent:
            graph[cur.val].append(parent.val)
            graph[parent.val].append(cur.val)
        if cur.left:
            self.build_graph(graph, cur.left, cur)
        if cur.right:
            self.build_graph(graph, cur.right, cur)

        return

    def bfs(self, graph, target, k):
        queue = [(target, 0)]
        visited = {target}
        res = []

        while queue:
            # 当前节点
            cur, distance = queue.pop(0)
            # 和思路1一样，只是这里用continue来继续进入下一个节点
            if distance == k:
                res.append(cur)
                continue

            for nei in graph[cur]:
                if nei not in visited:
                    queue.append((nei, distance + 1))
                    visited.add(nei)

        return res

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> [int]:
        """
        Time O(n)
        Space O(n)
        和思路1基本一致，区别在于不用改动树的结构，这里把树变成图，之后用BFS遍历。
        """
        graph = defaultdict(list)

        self.build_graph(graph, root, None)

        return self.bfs(graph, target.val, k)


node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(6)
node4 = TreeNode(2)
node1.left = node2
node2.left = node3
node2.right = node4
s = Solution2()
print(s.distanceK(node1, node2, 1))