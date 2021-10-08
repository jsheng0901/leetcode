# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def traversal(self, node, low, high):
        if node is None:
            return node

        if node.val > low:
            self.traversal(node.left, low, high)

        if low <= node.val <= high:
            self.result += node.val

        if node.val < high:
            self.traversal(node.right, low, high)

        return

    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
        """中序遍历，每次判断大小再进入不同的branch，然后中间节点计算sum"""
        if root:
            self.traversal(root, low, high)

        return self.result
