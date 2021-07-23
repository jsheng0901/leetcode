# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, nodep, nodeq):
        if nodep is None and nodeq is None:
            return True
        if nodep is None and nodeq is not None:
            return False
        elif nodep is not None and nodeq is None:
            return False
        elif nodep.val != nodeq.val:
            return False

        left = self.traversal(nodep.left, nodeq.left)
        right = self.traversal(nodep.right, nodeq.right)

        return left and right

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """前序遍历，两个树同时进行，同时判断"""
        return self.traversal(p, q)

