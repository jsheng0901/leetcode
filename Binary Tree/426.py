# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first = None
        self.prev = None

    def traversal(self, node):
        if node is None:
            return

        self.traversal(node.left)

        if self.prev:
            self.prev.right = node      # 双向连接node
            node.left = self.prev
        else:
            self.first = node       # 记录头结点，当prev不存在时候，说明找到了第一个最左下角的node

        self.prev = node

        self.traversal(node.right)

        return

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        中序遍历BST， 用previous指针记录上一个节点，每次到下一个时候双向连接prev 和 current，
        用first指针记录头结点，最后连接头结点和尾节点
        """
        if root:
            self.traversal(root)
            self.prev.right = self.first
            self.first.left = self.prev
            return self.first
        else:
            return None
