# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution1:
    def __init__(self):
        # 记录老节点和新节点的map
        # 注意这里要初始化一下map，因None节点的值可能存进字典
        self.node_to_copy = {None: None}

    def traversal(self, node):
        if node is None:
            return None

        # 前序遍历构建 deep copy 树
        copy_node = Node(node.val)
        copy_node.left = self.traversal(node.left)
        copy_node.right = self.traversal(node.right)
        # 构建map
        self.node_to_copy[node] = copy_node

        return copy_node

    def traversal_random(self, node):
        if node is None:
            return

        # 新节点
        new_node = self.node_to_copy[node]
        # 老节点的random节点
        old_node_random = node.random
        # 新节点的random节点
        new_node_random = self.node_to_copy[old_node_random]
        # 新节点random指针赋值
        new_node.random = new_node_random

        self.traversal_random(node.left)
        self.traversal_random(node.right)

        return

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time O(n)
        Space O(n)
        前序遍历构件树，然后再进行random点的赋值链接，注意random这里有一个小细节就是新的node的random指针链接的是新的node，而不是原本的节点。
        """
        # 前序遍历构建新的树
        new_root = self.traversal(root)
        # 再次前序遍历赋值新的树的random指针
        self.traversal_random(root)

        return new_root


class Solution2:
    def __init__(self):
        self.visited = {None: None}

    def traversal(self, node):
        if node is None:
            return None

        # 遇到过之前，直接return
        if node in self.visited:
            return self.visited[node]

        # 当前节点做copy并存进字典
        copy_node = Node(node.val)
        self.visited[node] = copy_node

        # 三条边逐一走一遍
        copy_node.left = self.traversal(node.left)
        copy_node.right = self.traversal(node.right)
        copy_node.random = self.traversal(node.random)

        return copy_node

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time O(n)
        Space O(n)
        其实这个题和133一模一样，把random想象成edge，整个树的copy也就是graph的copy，每个节点有三个edge，用一个visited字典防止走回头路。
        """
        return self.traversal(root)


node1 = Node(1)
node2 = Node(4)
node3 = Node(7)
node1.right = node2
node2.left = node3
node2.random = node3
node3.random = node1
s = Solution2()
print(s.copyRandomBinaryTree(node1))
