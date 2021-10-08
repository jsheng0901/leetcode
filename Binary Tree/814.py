# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node):
        if node is None:
            return 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        if left == 1 and right == 0:        
            node.right = None
        elif left == 0 and right == 1:
            node.left = None
        elif left == 0 and right == 0 and node.val == 0:
            return 0
        elif left == 0 and right == 0 and node.val == 1:
            node.left = None
            node.right = None

        return 1

    def pruneTree(self, root: [TreeNode]) -> [TreeNode]:
        """后序遍历，找到所有可能的返回值的情况，对应处理节点"""
        result = self.traversal(root)

        return None if result == 0 else root
