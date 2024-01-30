from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.leaf_nodes = []

    def build_graph(self, graph, cur, pre):
        # 当前节点是空节点，直接结束，空节点不进图
        if cur is None:
            return
        # 当前节点是叶子节点，记录下来，为后续BFS遍历所有叶子节点用
        if cur.left is None and cur.right is None:
            self.leaf_nodes.append(cur)

        # 如果父节点存在，说明存在一条edge
        if pre:
            # 记录进图
            graph[cur].append(pre)
            graph[pre].append(cur)

        # 左右递归
        self.build_graph(graph, cur.left, cur)
        self.build_graph(graph, cur.right, cur)

        return

    def bfs(self, distance, graph):
        # 记录good path
        count = 0
        # 遍历所有叶子结点
        for leaf in self.leaf_nodes:
            # 初始化列队
            queue = [(leaf, 0)]
            # 注意这个set初始化要放整个queue，不然set没办法loop tree node
            seen = set(queue)
            while queue:
                # 当前节点
                node, length = queue.pop(0)
                # 如果当前节点已经超过distance，直接结束BFS，说明此时queue里面的所有节点length都已经走远了
                if length > distance:
                    break
                # 如果当前节点是叶子节点并且不是loop的叶子节点，说明找打一条path，结果 +1
                if node != leaf and node.left is None and node.right is None and length <= distance:
                    count += 1

                # 把所有没有走过的邻居节点房间queue
                for nei in graph[node]:
                    if nei not in seen:
                        queue.append((nei, length + 1))
                        seen.add(nei)

        return count // 2

    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Time O(n + n_leaf * n)
        Space O(n)
        先把树转化成无向图，然后BFS遍历所有叶子结点到其它点的距离，如果遇到其它叶子结点并且在distance内，则说明找到一对path，
        最终结果要除以2，因为两个叶子节点会重复计算一次。这里比较耗时的是每个叶子结点需要遍历一次整个树或者说图。很多点重复走了好几次。
        """
        graph = defaultdict(list)
        # 转化成图
        self.build_graph(graph, root, None)

        return self.bfs(distance, graph)


class Solution2:
    def __init__(self):
        self.count = 0

    def traversal(self, node, distance):
        # 当前是空节点，返回空list
        if node is None:
            return []
        # 当前节点是叶子节点，返回[0]表示叶子节点到叶子节点的距离是0
        if node.left is None and node.right is None:
            return [0]

        left = self.traversal(node.left, distance)
        right = self.traversal(node.right, distance)
        # 遍历所有叶子节点的组合
        for i in left:
            for j in right:
                # 这里要 +2，因为我们的当前节点左右节点表示左右节点到叶子节点的距离，+2 表示当前节点到左右节点的距离
                if i + j + 2 <= distance:
                    self.count += 1

        # 这里要先合并左右节点返回结果，再表示当前节点到左右叶子结点的距离 +1
        return [i + 1 for i in left + right if i + 1 < distance]

    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Time O(n_leaf * n_leaf)
        Space O(n)
        此思路更快，后续遍历，我们每次返回当前节点到此节点下面所有叶子结点的距离，返回一个list，然后我们遍历所有距离的组合找到小于distance，
        则找到多少条path。这里时间复杂度只和叶子结点的个数相关，一般叶子结点个数远小于总节点个数。
        """
        self.traversal(root, distance)

        return self.count


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4
s = Solution2()
print(s.countPairs(root=node1, distance=3))
