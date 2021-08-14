# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def traversal(self, node, max_value):
        if node is None:
            return

        if node.val >= max_value:
            self.count += 1
            max_value = node.val

        self.traversal(node.left, max_value)
        self.traversal(node.right, max_value)

        return

    def goodNodes(self, root: TreeNode) -> int:
        """前序遍历，找最大值在每个path的时候，然后判断是不是good node"""
        if root:
            self.traversal(root, float('-inf'))

        return self.count