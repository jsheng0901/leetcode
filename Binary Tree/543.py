# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = float('-inf')

    def traversal(self, node, depth):
        if node is None:
            return 0

        left = self.traversal(node.left, depth)
        right = self.traversal(node.right, depth)

        if left + right > self.diameter:
            self.diameter = left + right

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: [TreeNode]) -> float:
        """
        Time O(n) 遍历所有node
        Space O(n) 递归占用
        记录每个节点的最大深度，同时记录最大diameter
        """
        if root:
            self.traversal(root, 0)

        return self.diameter
